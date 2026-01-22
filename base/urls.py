from django.urls import path
from . import views
urlpatterns = [
    path("", views.home, name='home'),
    path("blog_detail/<int:pk>/", views.blog_details, name="blog_detail"),
    path("create/", views.create, name="create"),
    path("update/<int:pk>/", views.update, name="update"),
    path("delete/<int:pk>/", views.delete, name="delete"),

]