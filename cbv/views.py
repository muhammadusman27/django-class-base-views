from itertools import count
from multiprocessing import context
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.views.generic import TemplateView, RedirectView
from .models import Post
# Create your views here.

class ExTemplate(TemplateView):
    template_name = 'cbv/ex2.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['name'] = 'Dexter Dark Passenger'
        context['message'] = 'Welcome back my dark passenger.'
        context['posts'] = Post.objects.all()
        return context


class PostPreLoadTaskView(RedirectView):
    #url = 'https://github.com/muhammadusman27/django-class-base-views'
    # permanent = HTTP status code returned (True = 301, False = 302, Default = False)
    pattern_name = 'cbv:singlepost'

    def get_redirect_url(self, *args, **kwargs):
        post = Post.objects.get(pk=kwargs['pk'])
        post.count = post.count + 1
        post.save()
        return super().get_redirect_url(*args, **kwargs)


class SinglePostView(TemplateView):
    template_name = 'cbv/ex4.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['posts'] = get_object_or_404(Post, pk=self.kwargs.get('pk'))
        return context