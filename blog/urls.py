from django.urls import path
from .views import home, about, PostListView

urlpatterns = [
    path('', PostListView.as_view(), name="blog-home"),
    path('about/', about, name="blog-about"),
]
