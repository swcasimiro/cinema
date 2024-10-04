from django.shortcuts import render, get_object_or_404, redirect
import requests
from .forms import CommentForm
from .models import Index, Category, Video, Comment


# https://kinopoiskapiunofficial.tech API рейтинга
base_url = "https://kinopoiskapiunofficial.tech/api/v2.2/films/1186526"
appid = {'X-API-KEY': 'f98a5461-d00d-4929-9a5c-e441318daba7'}



def index(request):
    index = Index.objects.all()
    category = Category.objects.all()
    response = requests.get(base_url, headers=appid)


    # отрабатывает исключения.
    if response.status_code == 200:
        response = requests.get(base_url, headers=appid)
    else:
        response = 'Недоступно'

    data = {
        'index': index,
        'category': category

        # api https://kinopoiskapiunofficial.tech
        # 'kinopoisk': response.json()['ratingKinopoisk'], # получаем рейтинг кинопоиска
        # 'imdb': response.json()['ratingImdb'], # получаем рейтин Imdb
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

    # form comment
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.video_c = video
            post.save()
            return redirect(f'/movie/{slug}/{slug_video}')

    else:
        form = CommentForm()

    # comment query
    comment_list = Comment.objects.filter(video_c=video).select_related('video_c')

    # reviews quantity
    comment_success = Comment.objects.filter(type_r='Положительная').filter(video_c=video).values('type_r')
    comment_danger = Comment.objects.filter(type_r='Отрицательная').filter(video_c=video).values('type_r')
    comment_neutral = Comment.objects.filter(type_r='Нейтральная').filter(video_c=video).values('type_r')

    # rating system - 5 points
    ranked = len(comment_success)*5 + len(comment_danger)
    len_comment = len(comment_success) + len(comment_danger)

    if len_comment:
        ranked = float(f"{ranked / len_comment:.{1}f}")
    else:
        ranked = 'Нет отзывов'


    data = {
        'video': video,
        'video_list': video_list,
        'cat': category,
        'form': form,
        'ranked': ranked,

        # comment info and list
        'comment_success': comment_success,
        'comment_danger': comment_danger,
        'comment_neutral': comment_neutral,
        'comment_list': comment_list,

        # api https://kinopoiskapiunofficial.tech
        # 'kinopoisk': response.json()['ratingKinopoisk'],  # получаем рейтинг кинопоиска
        # 'imdb': response.json()['ratingImdb'],  # получаем рейтин Imdb
    }

    return render(request, 'cinema/movie.html', data)
