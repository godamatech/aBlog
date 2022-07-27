from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .form import PostForm, EditForm
from django.urls import reverse_lazy
from django.shortcuts import render
from .models import Post


# def index(request):
#     return render(request, 'index.html', {'posts': Post.objects.all()})

class Home(ListView):
    model = Post
    template_name = 'index.html'
    ordering = ['-id']

class Details(DetailView):
    model = Post
    template_name = 'details.html'

class AddPost(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'add-post.html'
    # fields = '__all__'
    # fields = ('title','title_tag', 'body', 'author')

class UpdatePost(UpdateView):
    model = Post
    template_name = 'update-post.html'
    form_class = EditForm
    # fields = ( 'title', 'title_tag', 'body' )

class DeletePost(DeleteView):
    model = Post
    template_name = 'delete-post.html'
    success_url = reverse_lazy('home')
