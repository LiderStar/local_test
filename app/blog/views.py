from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView

from blog.forms import PostAdd, PostAddForm
from blog.models import Post
from django.shortcuts import get_object_or_404


# Create your views here.

def index(request):
    context = {"title": "Blog page"}
    return render(request, "blog/base_blog.html", context)


def signup(request):
    context = {"title": "Signup page"}
    return render(request, "blog/signup.html", context)


class UserPostListView(ListView):
    model = Post
    paginate_by = 50
    template_name = 'blog/user_posts.html'

    # def get_context_data(self, **kwargs):
    #     user = get_object_or_404(User, username=self.kwargs.get('username'))
    #     queryset = Post.objects.filter(author=user)
    #     context = super().get_context_data(**kwargs)
    #     context['users_posts'] = queryset.order_by('-title')
    #     return context
    context_object_name = 'users_posts'

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user.id).order_by('-title')


class AllPostListView(ListView):
    model = Post
    paginate_by = 50
    template_name = 'blog/all_posts.html'
    context_object_name = 'all_posts'

    def get_queryset(self):
        return Post.objects.all().order_by('-date_create')


def add_post(request):
    if request.method == "POST":
        form = PostAdd(request.POST)
        if form.is_valid():
            post = Post.objects.create(**form.cleaned_data)
            return redirect("all_posts_list")
    else:
        form = PostAdd()

    return render(request, "blog/add_post.html", {"form": form})


# def add_post2(request):
#     if request.method == "POST":
#         form = PostAddForm(request.POST)
#         if form.is_valid():
#             post = form.save()
#             return redirect("all_posts_list")
#     else:
#         form = PostAddForm()
#     return render(request, "blog/add_post_model.html", {"form": form})


class CreatePost(CreateView):
    form_class = PostAddForm
    template_name = "blog/add_post_model.html"
    success_url = reverse_lazy('all_posts_list')


class ViewPost(DetailView):
    model = Post
    template_name = "blog/view_post.html"
    context_object_name = 'post_item'
    # slug_url_kwarg = 'post_slug'

