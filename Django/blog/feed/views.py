from django.shortcuts import render, get_object_or_404
from django.views.generic import View

from .models import Post, Tag
from .utils import ObjectDetailmixin
from .forms import TagForm, PostForm

def posts_list(request):
    posts = Post.objects.all()
    return render(request,'feed/index.html', context = {'posts' : posts })


class PostCreate(View):
    def get(self, request):
        form = PostForm()
        return render(request, 'post/post_create.html', context={'form': form})

    def post(self, request):
        bound_form = PostForm(request.POST)
        if bound_form.is_valid():
            new_post = bound_form.save()
            return redirect(new_post)
        return render(request, 'post/post_create.html', context={'form':bound_form})


class PostDetail(ObjectDetailmixin, View):
    model = Post
    template = 'feed/post_detail.html'


class TagDetail(ObjectDetailmixin, View):
    model = Tag
    template = 'feed/tag_detail.html'


class TagCreate(View):
    def get(self, request):
        form = TagForm()
        return render(request, 'feed/tag_create.html', context = {'form' : form})


def tags_list(request):
    tags = Tag.objects.all()
    return render(request, 'feed/tags_list.html', context = {'tags' : tags})

