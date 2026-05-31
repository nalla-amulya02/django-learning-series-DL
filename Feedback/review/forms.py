from django import forms


class FeedbackForm(forms.Form):
    user_name = forms.CharField(
        label="Your Name",
        max_length=10,
        required = False,
        # error_messages={
        #     "required": "your username should not be empty",
        # }
    )


    