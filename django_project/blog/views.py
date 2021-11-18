from django.shortcuts import render
from django.http import HttpResponse


posts = [
    {
        'author' : 'Javeed',
        'title' : 'Blog 1',
        'content' : 'Content 1',
        'date_posted' : '23/18/1990'

    },
    {
        'author' : 'John',
        'title' : 'Blog 2',
        'content' : 'Content 2',
        'date_posted' : '27/18/1990'
    }
]

def home(request):
    context = {
        'posts' : posts
    }
    return render(request,'blog/home.html',context)


def about(request):
    return render(request,'blog/about.html',{'title':'About'})
