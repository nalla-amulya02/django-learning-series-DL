from django.http import HttpResponse
from django.shortcuts import render
from django.template.loader import render_to_string
# Create your views here.


def hello(request):
    # render_to_string
    # django looks for a templates folder in the app
    # converts html page into a string
    # html_content = render_to_string("hello/index.html")
    # return HttpResponse(html_content)
    student = ["a","b","c"]

    # render
    return render(request,"hello/index.html",{
        "student_names" : student
    })



    


# /hello/John
def hello_name( request, name):
    # return HttpResponse(f"Hello{name}")
    return render(request,'hello/name.html',{
        "name_anything": name,
    })
