import imp
from django.urls import path
from django.views.generic import TemplateView, RedirectView
from .views import ExTemplate, PostPreLoadTaskView, SinglePostView

app_name = 'cbv'

urlpatterns = [
    # Template View
    path('ex1/', TemplateView.as_view(template_name='cbv/ex1.html', extra_context={'title': 'Hello, World!'}), name='ex1'),
    path('ex2/', ExTemplate.as_view(), name='ex2'),

    # Redirect View
    path('rdt', RedirectView.as_view(url='https://www.youtube.com/watch?v=omgSWqwVTjY'), name='go-to-arcane'),
    path('ex3/<int:pk>/', PostPreLoadTaskView.as_view(), name='redirect-task'),
    path('ex4/<int:pk>', SinglePostView.as_view(), name='singlepost'),
]