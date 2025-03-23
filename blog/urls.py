from django.urls import path
from . import views


urlpatterns = [
    path("", views.start_page, name="start_page"),
    path("posts/", views.list_posts, name="list_posts"),
    path("posts/<slug:slug>", views.show_post, name="show_post"),
]
