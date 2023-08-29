
from django.urls import path
from blogs.apps import BlogsConfig
from blogs.views import BlogCreateView, BlogListView, BlogUpdateView, BlogDeleteView, BlogDetailView
app_name = BlogsConfig.name


urlpatterns = [
    path('', BlogListView.as_view(), name='blog_list'),
    path('create_blog', BlogCreateView.as_view(), name='create_blog'),
    path('edit_blog/<int:pk>/', BlogUpdateView.as_view(), name='edit_blog'),
    path('delete_blog/<int:pk>/', BlogDeleteView.as_view(), name='delete_blog'),
    path('view_blog/<int:pk>/', BlogDetailView.as_view(), name='view_blog')
]