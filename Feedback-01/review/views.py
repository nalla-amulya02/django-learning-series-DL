from urllib import request

from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import View

from review.forms import FeedbackForm
from review.models import Review
from django.views.generic.base import TemplateView
# Create your views here.
def index(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)

        if form.is_valid():
            # print(form.cleaned_data)
            # {'user_name' : 'Amulya'}


            # print("your feedback is submitted successfully - from main url")
            # name = request.POST["name"]
            # feedback = request.POST["feedback"]
            # rating = request.POST["rating"]

            # works for Form object but not for ModelForm object
            # name = form.cleaned_data["user_name"]
            # feedback = form.cleaned_data["feedback"]
            # rating = form.cleaned_data["rating"]
            # print(name, feedback, rating)

            # review = Review(user_name=name, review_text=feedback, rating=rating)
            # review.save()

            form.save()



            # print(name)
            return HttpResponseRedirect("/thank-you")
    


    form  = FeedbackForm()
    return render(request, 'review/review.html',{
        "form" : form
    })




class ReviewView(View):

    def get(self, request):
        form  = FeedbackForm()
        return render(request, 'review/review.html',{
            "form" : form
        })

    def post(self, request):
        form = FeedbackForm(request.POST)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/thank-you")
        





# def thanks(request):
#     print("your feedback is submitted successfully - from thank you url")
#     return render(request, 'review/thanks.html')


class ThanksView(TemplateView):
    template_name = 'review/thanks.html'





