from django.shortcuts import render, get_object_or_404
from django.views.generic import View

from .models import *

class ObjectDetailmixin:
    model = None
    template = None

    def get(self, request, slug):
        #  post = Post.objects.get(slug__iexact=slug)
        obj = get_object_or_404(Post, slug__iexact=slug)
        return render(request, self.template, context = { self.model.__name__.lower() : obj })