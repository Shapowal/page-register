from django.shortcuts import render
def index_platform(request):

    return render(request, 'third_task/platform.html', {"title": "ГЛАВНАЯ СТРАНИЦА"})



def index_games(request):

    return render(request, 'third_task/game.html', {"title": "ИГРЫ"})

def index_basket(request):

    return render(request, 'third_task/basket.html', {"title": "КОРЗИНА"})