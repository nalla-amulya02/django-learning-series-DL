from django.http import HttpResponse
from django.shortcuts import render
from django.template.loader import render_to_string
# Create your views here.
from .models import Student


def hello(request):
    # render_to_string
    # django looks for a templates folder in the app
    # converts html page into a string
    # html_content = render_to_string("hello/index.html")
    # return HttpResponse(html_content)
    student = ["John","Jane","Bob","Alice"]


# fetch students from db
    students = Student.objects.all()




    # render
    return render(request,"hello/index.html",{
        "student_names" : students
    })









# /hello/John
def hello_name( request, name):
    # return HttpResponse(f"Hello{name}")

    # /hello/xyz  -> name , age, address etc
    name_student = Student.objects.filter(name = "xyz")

    return render(request,'hello/name.html',{
        "name_anything": name_student ,
    })
