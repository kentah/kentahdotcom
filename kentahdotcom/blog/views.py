from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View, TemplateView, ListView

from .models import Blog


class Index(ListView):
    model = Blog
    template_name = '../templates/blog/index.html'

    def getTitleList(self, request, *args, **kwargs):
        titles = self.get_queryset().latest('posted')
        response = HttpResponse
        return response


