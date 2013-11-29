from django import forms


class RequestForm(forms.Form):
    email = forms.EmailField()


class CodeVerifyForm(forms.Form):
    code = forms.CharField(max_length=8)