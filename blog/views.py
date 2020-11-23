from django.shortcuts import render
from django.views.generic import View
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404
from .models import *
from .utils import ObjectDetailMixin
from .forms import TagForm


def post_list(request):
    posts = Post.objects.all()
    return render(request, 'blog/index.html', context={'posts': posts})


def tags_list(request):
    tags = Tag.objects.all()
    return render(request, 'blog/tags_list.html', context={'tags': tags})


class Post_detail(ObjectDetailMixin, View):
    template = 'blog/post_detail.html'
    model = Post


class Tag_detail(ObjectDetailMixin, View):
    template = 'blog/tag_detail.html'
    model = Tag


class TagCreate(View):
    def get(self, request):
        form = TagForm()
        return render(request, 'blog/tag_create_form.html', context={'form': form})

    def post(self, request):
        new_tag = TagForm(request.POST)

        if new_tag.is_valid():
            new_tag.new_slug
            new_tag.save()
            return redirect(new_tag)

        return render(request, 'blog/tag_create.html', context={'form': new_tag})






