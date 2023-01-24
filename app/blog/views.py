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

    # def get_context_data(self, **kwargs):
    #     user = get_object_or_404(User, username=self.kwargs.get('username'))
    #     queryset = Post.objects.filter(author=user)
    #     context = super().get_context_data(**kwargs)
    #     context['users_posts'] = queryset.order_by('-title')
    #     return context
    context_object_name = 'users_posts'
    
    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-title')



