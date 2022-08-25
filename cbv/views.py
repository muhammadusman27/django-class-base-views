from multiprocessing import context
from django.shortcuts import render

from django.views.generic import TemplateView
from .models import Post
# Create your views here.

class ExTemplate(TemplateView):
    template_name = 'cbv/ex2.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['name'] = 'Dexter Dark Passenger'
        context['message'] = 'Welcome back my dark passenger.'
        context['post'] = Post.objects.get(pk=1)
        return context
