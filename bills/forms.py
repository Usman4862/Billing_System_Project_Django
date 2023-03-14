from django import forms
from django.contrib.auth import get_user_model

class InfoForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(
			attrs={"class":"form-control",
			"placeholder":"Your Full Name"
			}
			))

    mobilenumber = forms.CharField(widget=forms.TextInput(
        attrs={"class": "form-control",
               "placeholder": "Your Mobile Number"
               }
    ))

    email = forms.EmailField(widget=forms.EmailInput(
			attrs={"class":"form-control",
			"placeholder":"Your Email"
			}
			))
