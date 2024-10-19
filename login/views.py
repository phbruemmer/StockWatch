from django.shortcuts import render
import hashlib
from login.models import *


def index(requests):
    if requests.method == 'POST':
        email = requests.POST.get('email')
        password = requests.POST.get('password')
        password = hashlib.sha256(password.encode()).hexdigest()
        print(email)
        print(password)
        print(User.objects.all())

    return render(requests, 'login_index.html')
