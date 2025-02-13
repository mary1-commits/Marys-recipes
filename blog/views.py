from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.db.models import Count
from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.views import generic, View
from django.contrib import messages
from django.http import HttpResponseRedirect, HttpResponseForbidden
from django.urls import reverse_lazy
from .models import Post, Comment
from .forms import CommentForm, PostForm

# List View for Blog Posts
class PostListView(generic.ListView):
    model = Post
    template_name = 'blog/index.html'
    context_object_name = 'posts'
    paginate_by = 10

    def get_queryset(self):
        queryset = Post.objects.filter(status=1) \
            .annotate(comment_count=Count('comments')) \
            .select_related('author')

        # Show all posts to staff users
        if self.request.user.is_staff:
            queryset = Post.objects.filter(status=1).annotate(
                comment_count=Count('comments')
            ).select_related('author')

        return queryset

class PostDraftListView(LoginRequiredMixin, generic.ListView):
    model = Post
    template_name = 'blog/index.html'
    context_object_name = 'posts'
    paginate_by = 10

    def get_queryset(self):
        queryset = Post.objects.filter(status=0, author=self.request.user) \
            .annotate(comment_count=Count('comments')) \
            .select_related('author')

        # Show all posts to staff users
        if self.request.user.is_staff:
            queryset = Post.objects.filter(status=0).annotate(
                comment_count=Count('comments')
            ).select_related('author')

        return queryset
# Detail View for a Single Blog Post
class PostDetailView(generic.DetailView):
    model = Post
    template_name = 'blog/post_detail.html'
    context_object_name = 'post'

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.annotate(comment_count=Count('comments')) \
            .select_related('author')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comments'] = self.object.comments.all().select_related('author')
        context['comment_count'] = self.object.comments.all().count()
        context['comment_form'] = CommentForm()
        return context



class PostCreateView(LoginRequiredMixin, generic.CreateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/post_form.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        # Get cleaned data from the form
        title = form.cleaned_data['title']
        content = form.cleaned_data['content']
        featured_image = form.cleaned_data['featured_image']
        excerpt = form.cleaned_data['excerpt']

        post = Post(
            title=title,
            author=self.request.user,
            content=content,
            featured_image=featured_image,
            excerpt=excerpt,
            status=0,
        )

        # Save the post
        post.save()

        # Redirect to success URL
        return redirect(self.success_url)

    def form_invalid(self, form):
        # Handle invalid form
        return self.render_to_response(
            self.get_context_data(form=form)
        )

class PostUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/post_form.html'
    context_object_name = 'post'

    def get_success_url(self):
        return reverse_lazy('post_detail', kwargs={'slug': self.object.slug})

    def get_queryset(self):
        # Users can only edit their own posts unless they are staff
        if self.request.user.is_staff:
            return Post.objects.all()
        return Post.objects.filter(author=self.request.user)



def delete_post(request, slug):
    post = get_object_or_404(Post, slug=slug)
    if request.user != post.author:
        messages.error(request, "You don't have permission to delete this post.")
        return HttpResponseForbidden("You don't have permission to delete this post.")

    post.delete()
    messages.success(request, 'Post deleted successfully!')

    return redirect('home')


def publish_post(request, slug):
    post = get_object_or_404(Post, slug=slug)
    # Check if the user is the author of the post
    if request.user != post.author:
        messages.error(request, "You don't have permission to publish this post.")
        return HttpResponseForbidden("You don't have permission to publish this post.")

    # Validate comment isn't already approved
    if post.status != 0:
        messages.warning(request, "This post is already published.")
        return redirect('post_detail', slug=post.slug)

    # Approve the comment
    post.status = 1
    post.save()

    # Add success message
    messages.success(request, "Post has been published successfully.")

    # Redirect back to the post detail page
    return redirect('post_detail', slug=post.slug)



def add_comment(request, pk):
    post = get_object_or_404(Post, pk=pk)

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            # Get the cleaned data from the form
            comment_body = form.cleaned_data['body']

            # Create new comment instance manually
            comment = Comment(
                post=post,
                author=request.user,
                body=comment_body,
                approved=False
            )

            # Save the comment
            comment.save()

            return redirect('post_detail', slug=post.slug)
    else:
        form = CommentForm()

    return render(request, 'blog/post_detail.html', {'form': form, 'post': post})

# Edit Comment View
def comment_edit(request, slug, comment_id):
    comment = get_object_or_404(Comment, pk=comment_id, author=request.user)
    
    if request.method == "POST":
        comment_form = CommentForm(request.POST, instance=comment)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.approved = False  # Requiring re-approval after edits
            comment.save()
            messages.success(request, 'Comment updated successfully!')
        else:
            messages.error(request, 'Error updating comment!')

    return HttpResponseRedirect(reverse('post_detail', args=[slug]))


@login_required
def approve_comment(request, comment_id):
    # Get the comment or return 404
    comment = get_object_or_404(Comment, id=comment_id)

    # Check if the user is the author of the post
    if request.user != comment.post.author:
        messages.error(request, "You don't have permission to approve this comment.")
        return HttpResponseForbidden("You don't have permission to approve this comment.")

    # Validate comment isn't already approved
    if comment.approved:
        messages.warning(request, "This comment is already approved.")
        return redirect('post_detail', slug=comment.post.slug)

    # Approve the comment
    comment.approved = True
    comment.save()

    # Add success message
    messages.success(request, "Comment has been approved successfully.")

    # Redirect back to the post detail page
    return redirect('post_detail', slug=comment.post.slug)


# Delete Comment View
def comment_delete(request, comment_id):
    comment = get_object_or_404(Comment, pk=comment_id, author=request.user)
    if request.user != comment.author:
        messages.error(request, "You don't have permission to delete this comment.")
        return HttpResponseForbidden("You don't have permission to delete this comment.")

    comment.delete()
    messages.success(request, 'Comment deleted successfully!')

    return redirect('post_detail', slug=comment.post.slug)


# Dynamic Recipe Detail View (For all Somali recipes)
def recipe_detail(request, slug):
    recipe = get_object_or_404(Post, slug=slug, status=1)  # Assuming recipes are also Posts
    return render(request, "blog/post_detail.html", {"post": recipe})
