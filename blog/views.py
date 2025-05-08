from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import View
from django.views.generic import ListView
from django.urls import reverse

from .forms import CommentForm
from .models import Post


class StartPageView(ListView):
    template_name = "blog/start_page.html"
    model = Post
    ordering = ["-date"]
    context_object_name = "posts"

    def get_queryset(self):
        qs = super().get_queryset()
        data = qs[:3]
        return data


class ListPostsView(ListView):
    template_name = "blog/all_posts.html"
    model = Post
    ordering = ["-date"]
    context_object_name = "all_posts"


class PostDetailView(View):
    def get(self, request, slug):
        post = Post.objects.get(slug=slug)
        context = {
            "post": post,
            "comment_form": CommentForm(),
            "post_tags": post.tags.all(),
            "comments": post.comments.all().order_by("-id"),
        }
        return render(request, "blog/post_detail.html", context)

    def post(self, request, slug):
        form = CommentForm(request.POST)
        post = Post.objects.get(slug=slug)

        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()

            return HttpResponseRedirect(reverse("show_post", args=[slug]))

        context = {
            "post": post,
            "comment_form": form,
            "post_tags": post.tags.all(),
            "comments": post.comments.all().order_by("-id"),
        }

        return render(request, "blog/post_detail.html", context)
