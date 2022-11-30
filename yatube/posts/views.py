from django.shortcuts import render, get_object_or_404
# from django.http import HttpResponse
# Импортируем загрузчик.
# from django.template import loader
# для финального
from .models import Group, Post
# Create your views here.


def index(request):
    title = 'Последние обновления на сайте'
    posts = Post.objects.all()[:10]
    context = {
        'posts': posts,
        'title': title,
    }
    return render(request, 'posts/index.html', context)


def group_posts(request, slug):
    group = get_object_or_404(Group, slug=slug)
    title = f'Записи сообщества {group}'
    posts = group.posts.all()[:10]
    context = {
        'group': group,
        'title': title,
        'posts': posts,
    }
    return render(request, 'posts/group_list.html', context)
# до вывода инф из БД
# Главная страница
# def index(request):
#    template = 'posts/index.html'
#    title = 'Это главная страница проекта Yatube'
#    context = {
#        'title': title,
#    }
#    return render(request, template, context)
# def group_posts(request, slug):
#    template = 'posts/group_list.html'
#    title = 'Здесь будет информация о группах проекта Yatube'
#    context = {
#        'title': title,
#    }
#    return render(request, template, context)
