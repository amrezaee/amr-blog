from django.shortcuts import render


def start_page(request):
    return render(request, "blog/start_page.html")


def list_posts(request):
    return render(request, "blog/all_posts.html")


def show_post(request, slug):
    return render(request, "blog/post_detail.html")
