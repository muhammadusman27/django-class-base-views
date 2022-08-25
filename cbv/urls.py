import imp
from django.urls import path
from django.views.generic import TemplateView
from .views import ExTemplate

urlpatterns = [
    path('ex1/', TemplateView.as_view(template_name='cbv/ex1.html', extra_context={'title': 'Hello, World!'}), name='ex1'),
    path('ex2/', ExTemplate.as_view(), name='ex2'),
]