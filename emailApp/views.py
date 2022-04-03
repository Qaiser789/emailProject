from django.shortcuts import render
from .forms import EmailsForm
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.


def sendEmails(request):
    messageSent = False
    if request.method == 'POST':
        form = EmailsForm(request.POST)
        if form.is_valid():
            cd= form.cleaned_data
            subject = cd['subject']
            message = cd['message']
            send_mail(subject, message, settings.EMAIL_HOST_USER, [cd['email']])
            messageSent = True

    form= EmailsForm()
    return render(request, 'index.html', context={'form': form, 'messageSent': messageSent,})
