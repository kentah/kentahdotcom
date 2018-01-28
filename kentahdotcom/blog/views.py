from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View

from .models import Blog, Category


class Index(View):
    model = Blog

    def get(self, request, *args, **kwargs):
        return HttpResponse('It works')
