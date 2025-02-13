from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic, View
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Post, Comment
from .forms import CommentForm

# List View for Blog Posts
class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1)
    template_name = "blog/index.html"
    paginate_by = 6
    context_object_name = "posts"

# Detail View for a Single Blog Post with Comments
def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug, status=1)
    comments = post.comments.filter(approved=True).order_by("-created_on")
    comment_count = comments.count()
    comment_form = CommentForm()

    if request.method == "POST":
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.author = request.user
            comment.post = post
            comment.save()
            messages.success(request, "Comment submitted and awaiting approval!")
            return redirect("post_detail", slug=slug)

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

# Edit Comment View
def comment_edit(request, slug, comment_id):
    comment = get_object_or_404(Comment, pk=comment_id, author=request.user)

    if request.method == "POST":
        comment_form = CommentForm(request.POST, instance=comment)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.approved = False  # Require re-approval after edits
            comment.save()
            messages.success(request, "Comment updated successfully!")
        else:
            messages.error(request, "Error updating comment!")

        return redirect("post_detail", slug=slug)

    return render(request, "blog/edit_comment.html", {"comment_form": CommentForm(instance=comment)})

# Delete Comment View
def comment_delete(request, slug, comment_id):
    comment = get_object_or_404(Comment, pk=comment_id, author=request.user)

    if request.method == "POST":
        comment.delete()
        messages.success(request, "Comment deleted successfully!")
        return redirect("post_detail", slug=slug)

# Recipe Detail View (For Somali Recipes)
def recipe_detail(request, slug):
    recipe = get_object_or_404(Post, slug=slug, status=1)
    return render(request, "blog/post_detail.html", {"post": recipe})
