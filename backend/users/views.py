from django.shortcuts import render, redirect, HttpResponseRedirect
from django.views import View
from .models import author
from django.contrib.auth.hashers import check_password, make_password
from blog.models import *


class author_register(View):
    def get(self, request):
        return render(request, 'register.html')
    
    def post(self, request):
        if(author.get_auth_by_username(request.POST.get('username'))):
            return render(request, 'register.html', {'error': 'The username already exists.'})
        author_obj = author()
        author_obj.username = request.POST['username']
        pass1 = request.POST.get('password1')
        pass2 = request.POST.get('password2')
        if(pass1 != pass2):
            return render(request, 'register.html', {'error': "Password doesn't match."})
        author_obj.name = request.POST['name']
        author_obj.email = request.POST['email']
        author_obj.phno = request.POST['number']
        author_obj.password = make_password(pass1)
        author_obj.save()
        #request.session['author'] = author_obj
        return redirect('/login/')

class author_login(View):
    def get(self, request):
        return render(request, 'login.html', {'title': 'Login'})
    
    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        author_obj = author.get_auth_by_username(username)
        if(author_obj):
            if(check_password(password, author_obj.password)):
                request.session['auth_id'] = author_obj.id
                request.session['img_url'] = author_obj.image.url
                return HttpResponseRedirect('/profile')
        else:
            return render(request, 'login.html', {'error': 'Wrong Username or Password', 'title': 'Login'})
        return render(request, 'login.html', {'title': 'Login'})

def logout_author(request):
    request.session.clear()
    return redirect('/')

class author_profile(View):
    def get(self, request):
        author_obj = author.objects.get(id = request.session['auth_id'])
        posts = Post.objects.filter(author_id = request.session['auth_id'])
        return render(request, 'profile.html', {'author': author_obj, 'posts': posts, 'title': 'Profile'})