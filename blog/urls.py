from django.urls import path
from . import views


urlpatterns = [
    path("", views.StartPageView.as_view(), name="start_page"),
    path("posts/", views.ListPostsView.as_view(), name="list_posts"),
    path("posts/<slug:slug>", views.PostDetailView.as_view(), name="show_post"),
]
