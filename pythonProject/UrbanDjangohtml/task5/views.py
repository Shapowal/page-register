from django.shortcuts import render
from .forms import UserRegister

# Псевдо-список пользователей
users = ["existing_user1", "existing_user2", "existing_user3"]

def sign_up_by_django(request):
    info = {}
    if request.method == 'POST':
        form = UserRegister(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            repeat_password = form.cleaned_data.get('repeat_password')
            age = form.cleaned_data.get('age')

            if password != repeat_password:
                info['error'] = 'Пароли не совпадают'
            elif age < 18:
                info['error'] = 'Вы должны быть старше 18'
            elif username in users:
                info['error'] = 'Пользователь уже существует'
            else:
                info['message'] = f"Приветствуем, {username}!"
                users.append(username)
        info['form'] = form
    else:
        form = UserRegister()
        info['form'] = form

    return render(request, 'fifth_task/registration_page.html', info)

def sign_up_by_html(request):
    info = {}
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        repeat_password = request.POST.get('repeat_password')
        try:
            age = int(request.POST.get('age', 0))
        except ValueError:
            info['error'] = 'Некорректное значение возраста'

        if 'error' not in info:
            if password != repeat_password:
                info['error'] = 'Пароли не совпадают'
            elif age < 18:
                info['error'] = 'Вы должны быть старше 18'
            elif username in users:
                info['error'] = 'Пользователь уже существует'
            else:
                info['message'] = f"Приветствуем, {username}!"
                users.append(username)

    if request.method == 'GET':
        info['username'] = ''
        info['age'] = 0

    return render(request, 'fifth_task/registration_page.html', info)