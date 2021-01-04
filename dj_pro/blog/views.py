from django.shortcuts import render


posts=[
    {
        'author':'Prachi Nandi',
        'title': 'Blog post 1',
        'content': 'first post content',
        'date_posted': '6 nov,2020 '
    },
    {
        'author': 'Pratyush Nandi',
        'title': 'Blog post 2',
        'content': 'second post content',
        'date_posted': '21 nov,2020 '
    }
]

def home(request):
    context={'posts' : post }
    return render(request, 'blog/home.html',context)

def about(request):
    return render(request, 'blog/about.html')