from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View, TemplateView, ListView


class Visual(TemplateView):
    template_name = '../templates/visual/visual.html'