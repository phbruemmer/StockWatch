from django.shortcuts import render
import hashlib
from login.models import *


def index(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        password = hashlib.sha256(password.encode()).hexdigest()
        user_id = User.objects.get(email=email).id()
        if password == User.objects.get(id=user_id).password():
            print("success!")
        print(email)
        print(password)

    return render(request, 'login_index.html')


def register(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        username = request.POST.get('username')
        pw_1 = request.POST.get('pw_1')
        pw_2 = request.POST.get('pw_2')
        if pw_1 == pw_2:
            pw_1 = hashlib.sha256()

    return render(request, 'register_index.html')



