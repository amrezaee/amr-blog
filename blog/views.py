from django.shortcuts import render, get_object_or_404

from .models import Post, Author, Tag

def start_page(request):
    latests_posts = Post.objects.all().order_by("-date")[:2]
    return render(request, "blog/start_page.html",{
        "posts": latests_posts
    })


def list_posts(request):
    all_posts = Post.objects.all().order_by("-date")
    return render(request, "blog/all_posts.html", {
        "all_posts": all_posts
    })


def show_post(request, slug):
    post = get_object_or_404(Post, slug=slug)
    return render(request, "blog/post_detail.html",{
        "post": post,
        "post_tags": post.tags.all()
    })
