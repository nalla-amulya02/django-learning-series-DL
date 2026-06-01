from django import forms

from review.models import Review


# class FeedbackForm(forms.Form):
#     user_name = forms.CharField(
#         label="Your Name",
#         max_length=10,
#         # required = False,
#         error_messages={
#             "required": "your username should not be empty",
#         }
#     )
#     feedback = forms.CharField(
#         label="Your Feedback",
#         widget=forms.Textarea,
#         max_length=100,
#     )
#     rating = forms.IntegerField(
#         label="Your Rating from 1 to 10",
#         min_value=1,
#         max_value=10,
#     )



class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = "__all__"
        # fields = ["user_name","review_text"]

        # exclude = ["user_name"]
        labels = {
            "user_name": "Your Name",
            "review_text": "Your Feedback",
            "rating": "Your Rating from 1 to 10",
        }



    