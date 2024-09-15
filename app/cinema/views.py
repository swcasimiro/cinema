from django.shortcuts import render
import requests
from .models import Index, Category, Video


# https://kinopoiskapiunofficial.tech API рейтинга
base_url = "https://kinopoiskapiunofficial.tech/api/v2.2/films/1186526"
appid = {'X-API-KEY': 'f98a5461-d00d-4929-9a5c-e441318daba7'}



def index(request):
    response = requests.get(base_url, headers=appid)
    index = Index.objects.all()
    category = Category.objects.all()


    # отрабатывает исключения.
    if response.status_code == 200:
        response = requests.get(base_url, headers=appid)
    else:
        response = 'Недоступно'

    data = {
        'kinopoisk': response.json()['ratingKinopoisk'], # получаем рейтинг кинопоиска
        'imdb': response.json()['ratingImdb'], # получаем рейтин Imdb
        'index': index,
        'category': category
    }

    return render(request, 'cinema/index.html', data)


def movie(request):
    video = Video.objects.all()

    data = {
        'video': video
    }

    return render(request, 'cinema/movie.html', data)
