from django.shortcuts import render


def index(requests):
    if requests.method == 'POST':
        email = requests.POST.get('email')
        password = requests.POST.get('password')
        print(email)
        print(password)
    return render(requests, 'login_index.html')
