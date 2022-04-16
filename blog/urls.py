from django.urls import path
from .views import *
from . import views
from users.middleware.auth import authmiddleware


urlpatterns = [
    path('', PostListView.as_view(), name='blog-home'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', authmiddleware(newpost.as_view()), name='post-create'),
    path('post/<int:pk>/update/', (PostUpdateView.as_view()), name='post-update'),
    path('post/<int:pk>/delete/', (PostDeleteView.as_view()), name='post-delete'),
    path('post/<int:pk>/comment/', (PostComment.as_view()), name='post-delete'),
    path('about/', views.about, name='about'),
]