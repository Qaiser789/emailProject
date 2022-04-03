from django import forms

class EmailsForm(forms.Form):
    email = forms.EmailField(label='Email', max_length=500)
    subject = forms.CharField(label='Subject', max_length=100)
    message = forms.CharField(label='Message', widget=forms.Textarea)