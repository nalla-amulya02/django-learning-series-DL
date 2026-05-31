from urllib import request

from django.http import HttpResponseRedirect
from django.shortcuts import render

from review.forms import FeedbackForm

# Create your views here.
def index(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)

        if form.is_valid():
            print(form.cleaned_data)
        # {'user_name' : 'Amulya'}


        # print("your feedback is submitted successfully - from main url")
        # name = request.POST["name"]
        # email = request.POST["email"]
        # print(name)
        # return HttpResponseRedirect("/thank-you")
    


    form  = FeedbackForm()
    return render(request, 'review/review.html',{
        "form" : form
    })


def thanks(request):
    print("your feedback is submitted successfully - from thank you url")
    return render(request, 'review/thanks.html')
