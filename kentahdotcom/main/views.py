from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View, TemplateView, ListView


class Main(TemplateView):
    template_name = '../templates/main/main.html'


