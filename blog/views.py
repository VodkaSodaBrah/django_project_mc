from django.shortcuts import render
from django.http import HttpRequest, HttpResponse

posts = [
    {
        'author': 'Michael',
        'title': 'Post 1',
        'content': 'content',
        'date_posted': 'Aug 234324, 345453'
    },
    {
        'author': 'Mich',
        'title': 'Post 2',
        'content': 'content2',
        'date_posted': 'Aufgdfg34324, 345453'
    },
]

def home(request):
    context = {
        'posts': posts,
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})

