from django.http import HttpResponse
from django.shortcuts import redirect, render
from accounts.forms import RegisterForm
from accounts.models import Student
from django.contrib.auth.decorators import login_required, permission_required
# Create your views here.

def home(request):
    return render(request,'home.html')


def register(request):

    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        
    
    else:
        form = RegisterForm()
    return render(request,'register.html',{'form': form})


@login_required
def dashboard(request):
    return render(request,'dashboard.html')


@permission_required('accounts.view_student', raise_exception=True)
def student_list(request):
    students = Student.objects.all()

    return render(
        request,
        'student_list.html',
        {'students': students}
    )


@permission_required('accounts.add_student', raise_exception=True)
def add_student(request):

    Student.objects.create(
        name="New Student",
        email="new@gmail.com"
    )


    return HttpResponse("Student Added")



@permission_required('accounts.change_student', raise_exception=True)
def edit_student(request, id):

    student = Student.objects.get(id=id)

    student.name = "Updated Name"

    student.save()

    return HttpResponse("Updated")



@permission_required('accounts.delete_student', raise_exception=True)
def delete_student(request, id):

    student = Student.objects.get(id=id)

    student.delete()

    return HttpResponse("Deleted")
# built-in LoginView searches for -> registration/login.html