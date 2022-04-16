from django.urls import path
from django.contrib import admin
from django.contrib.auth import views as auth_views
from .views import *
from .middleware.auth import authmiddleware


urlpatterns = [
    path('login/', author_login.as_view(), name='login'),
    path('admin/', admin.site.urls),
    path('register/', author_register.as_view(),name='register'),
    path('profile/', authmiddleware(author_profile.as_view()), name='profile'),
    path('logout/', authmiddleware(logout_author), name='logout'),
]
