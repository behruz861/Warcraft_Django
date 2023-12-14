from django.shortcuts import render
from django.views.generic import TemplateView, ListView

from .models import Picture, Video, Audio


class StartPageView(TemplateView):
    template_name = 'warcraft/home.html'


class AboutPageView(TemplateView):
    template_name = 'warcraft/about.html'


class PhotoListView(ListView):
    template_name = 'warcraft/photo.html'
    model = Picture


class VideoListView(ListView):
    template_name = 'warcraft/video.html'
    model = Video


class AudioListView(ListView):
    template_name = 'warcraft/audio.html'
    model = Audio