from django.shortcuts import render
#from django.http import HttpResponse

# Create your views here.

posts = [
    {
        "author":"lakshman bharathi"
        , "title":"Test post"
        , "content":"My first django post"
        , "posted_on":"21:25 28-Oct-2023"
    }
    ,
    {
        "author":"lb"
        , "title":"Test post"
        , "content":"My second django post"
        , "posted_on":"21:26 28-Oct-2023"
    }
]

def home(request):
    context = {
        "posts":posts
    }
    return render(request=request, template_name="blog/home.html", context=context)

def about(request):
    return render(request=request, template_name="blog/about.html")
