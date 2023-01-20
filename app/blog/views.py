from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView
from blog.models import Post
from django.shortcuts import get_object_or_404


# Create your views here.

def blog(request):
    return HttpResponse("Hello", request)


class UserPostListView(ListView):
    model = Post
    paginate_by = 50
    template_name = 'blog/user_posts.html'
    context_object_name = 'users_posts'
    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user.id).order_by('-title')

