from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic, View
from django.contrib import messages
from django.http import HttpResponseRedirect
from .models import Post, Comment
from .forms import CommentForm

# List View for Blog Posts
class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1)
    template_name = "blog/index.html"
    paginate_by = 6
    context_object_name = "posts"

# Detail View for a Single Blog Post
class PostDetail(generic.DetailView):
    model = Post
    template_name = "blog/post_detail.html"
    context_object_name = "post"

# Function-Based View for Blog Post Details & Comments
def post_detail(request, slug):
    queryset = Post.objects.filter(status=1)
    post = get_object_or_404(queryset, slug=slug)
    comments = post.comments.filter(approved=True).order_by("-created_on")
    comment_count = post.comments.filter(approved=True).count()
    comment_form = CommentForm()

    if request.method == "POST":
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.author = request.user
            comment.post = post
            comment.save()
            messages.success(request, 'Comment submitted and awaiting approval!')
            return HttpResponseRedirect(reverse('post_detail', args=[slug]))

    return render(
        request,
        "blog/post_detail.html",
        {
            "post": post,
            "comments": comments,
            "comment_count": comment_count,
            "comment_form": comment_form,
        }
    )

# Create Comment View
class CommentCreateView(View):
    def post(self, request, slug):
        post = get_object_or_404(Post, slug=slug)
        comment_form = CommentForm(data=request.POST)
        
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.author = request.user
            comment.post = post
            comment.save()
            messages.success(request, 'Comment submitted and awaiting approval!')
        else:
            messages.error(request, 'Error submitting comment!')

        return HttpResponseRedirect(reverse('post_detail', args=[slug]))

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

# Delete Comment View
def comment_delete(request, slug, comment_id):
    comment = get_object_or_404(Comment, pk=comment_id, author=request.user)

    if request.method == "POST":
        comment.delete()
        messages.success(request, 'Comment deleted successfully!')

    return HttpResponseRedirect(reverse('post_detail', args=[slug]))

# Dynamic Recipe Detail View (For all Somali recipes)
def recipe_detail(request, slug):
    recipe = get_object_or_404(Post, slug=slug, status=1)  # Assuming recipes are also Posts
    return render(request, "blog/post_detail.html", {"post": recipe})
