from django.shortcuts import render, get_object_or_404
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


def movie(request, slug, slug_video):
    # api kinopoisk
    response = requests.get(base_url, headers=appid)

    if response.status_code == 200:
        response = requests.get(base_url, headers=appid)
    else:
        response = 'Недоступно'

    # video model + category models detail
    video = Video.objects.select_related('cat').get(slug=slug_video)
    category = get_object_or_404(Category, slug=slug)
    video_list = Video.objects.select_related('cat').filter(cat=category)

    data = {
        'video': video,
        'video_list': video_list,
        'cat': category,
        'kinopoisk': response.json()['ratingKinopoisk'],  # получаем рейтинг кинопоиска
        'imdb': response.json()['ratingImdb'],  # получаем рейтин Imdb
    }

    return render(request, 'cinema/movie.html', data)
