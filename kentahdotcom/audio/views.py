from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View, TemplateView, ListView


class Audio(TemplateView):
    template_name = '../templates/audio/audio.html'