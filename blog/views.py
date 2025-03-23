from django.shortcuts import render


def start_page(request):
    return render(request, "blog/start_page.html")


def list_posts(request):
    pass


def show_post(request):
    pass
