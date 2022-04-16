from django.shortcuts import redirect, render
from django.views.generic import ListView
from django.views import View
from .models import Post, Comment
from users.models import *
from .function import *


def home(request):
    context = {
        'posts': Post.objects.all(),
        'title': 'Home'
    }
    return render(request, 'home.html', context)


class newpost(View):
    def get(self, request):
        return render (request, 'post_form.html', {'title': 'New Post'})
    
    def post(self, request):
        post_obj = Post()
        post_obj.author_id = author.objects.get(id = request.session.get('auth_id'))
        post_obj.content = request.POST['body']
        post_obj.title = request.POST['title']
        post_obj.header_image = request.FILES['header_img']
        post_obj.save()
        if(request.POST['caption']):
            post_obj.img_caption = request.POST['caption']
            post_obj.save()
        else:
            post_obj.img_caption = generate_caption('./' + post_obj.header_image.url)
            post_obj.save()
        return redirect('profile')


class PostListView(ListView):
    model = Post
    template_name = 'home.html'  
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 5


class PostDetailView(View):
    def get(self, request, pk):
        post_obj = Post.objects.get(id = int(pk))
        com_obj = Comment.objects.filter(post = pk)
        return render(request, 'post_detail.html', {'object': post_obj, 'title': 'Post', 'title': 'Post', 'comments': com_obj})


class PostComment(View):
    def post(self, request, pk):
        obj = Comment()
        obj.post = Post.objects.get(id = pk)
        obj.name = request.POST.get('name')
        obj.body = request.POST.get('body')
        obj.save()
        return redirect('/post/'+str(pk))


class PostUpdateView(View):
    def get(self, request, pk):
        obj = Post.objects.get(id = pk)
        return render(request, 'post_edit.html', {'post': obj})

    def post(self, request, pk):
        obj = Post.objects.get(id = pk)
        if(request.POST.get('title', False)):
            obj.title = request.POST['title']
        if(request.POST.get('caption', False)):
            obj.img_caption = request.POST['caption']
        if(request.POST.get('body', False)):
            obj.content = request.POST['body']
        if(request.FILES.get('header_img', None) != None):
            obj.header_image = request.FILES['header_img']
        obj.save()
        obj = Post.objects.get(id = pk)
        return redirect('/post/'+str(pk))


class PostDeleteView(View):
    def get(self, request, pk):
        obj = Post.objects.get(id = pk)
        obj.delete()
        return redirect('/profile')


def about(request):
    return render(request, 'about.html', {'title': 'About', 'title': 'About us'})