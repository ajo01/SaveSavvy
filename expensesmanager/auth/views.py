from django.shortcuts import render
from django.views import View
import json
from django.http import JsonResponse
from django.contrib.auth.models import User
from validate_email import validate_email
from django.contrib import messages
import smtplib
from django.core.mail import EmailMessage
import os

# Create your views here.


class UsernameValidationView(View):
    def post(self, request):
        data = json.loads(request.body)
        username = data['username']

        if not str(username).isalnum():
            return JsonResponse({'username_error': 'Username should only contain alphanumberic characters'}, status=400)
        if User.objects.filter(username=username).exists():
            return JsonResponse({'username_error': 'The username already in use. Choose another username'}, status=409)
        return JsonResponse({'username_valid': True})


class EmailValidationView(View):
    def post(self, request):
        data = json.loads(request.body)
        email = data['email']

        if not validate_email(email):
            return JsonResponse({'email_error': 'Email is invalid'}, status=400)
        if User.objects.filter(email=email).exists():
            return JsonResponse({'email_error': 'The email already in use'}, status=409)
        return JsonResponse({'email_valid': True})


class RegistrationView(View):
    def get(self, request):
        return render(request, 'auth/register.html')

    def post(self, request):

        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        context = {
            'fieldValues': request.POST
        }

        if not User.objects.filter(username=username).exists():
            if not User.objects.filter(email=email).exists():
                if len(password) < 6:
                    messages.error(
                        request, 'Password must be at least 6 characters long')
                    return render(request, 'auth/register.html', context)
                user = User.objects.create_user(username=username, email=email)
                user.set_password(password)
                user.is_active = False
                user.save()

                send_email(email)

                messages.success(
                    request, 'Your account has been created!')
                return render(request, 'auth/register.html')
        return render(request, 'auth/register.html')


def send_email(email):
    MyEmail = os.environ['EMAIL_HOST_USER']
    MyPassword = os.environ['EMAIL_HOST_PASSWORD']

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login(MyEmail, MyPassword)
    email_subject = "Activate your account"
    email_body = "Test body"
    msg = f"Subject: {email_subject}\n\n{email_body}"
    # from MyEmail to email
    server.sendmail(MyEmail, email, msg)
    server.close()
    print('Email has been sent')
