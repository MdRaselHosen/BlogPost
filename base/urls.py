from django.urls import path
from . import views
urlpatterns = [
    path("", views.home, name='home'),
    path("blog_detail/<int:pk>", views.blog_details, name="blog_detail")
]