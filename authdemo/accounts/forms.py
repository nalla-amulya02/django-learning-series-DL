from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RegisterForm(UserCreationForm):

    class Meta:
        model = User #-> table for storing the creds automatically by django
        fields = ['username', 'email', 'password1']


# credentials - username, email, password

# john -  johnpassword@123  -->  hashing ->kpim......234 -> asneufeuvn