from django import forms

class Confirm(forms.Form):
    Email = forms.EmailField()
    def __str__(self):
        return self.Email