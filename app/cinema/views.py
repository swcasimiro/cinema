from django.shortcuts import render, get_object_or_404, redirect
from .forms import CommentForm
from .models import Index, Category, Video, Comment
from django.contrib.humanize.templatetags.humanize import intcomma
# import business logic
# from .services import points, appid, base_url, response
from .services import MovieService
from .tasks import api_ranked, test_api


def index(request):
    index = Index.objects.all()
    category = Category.objects.all()


    data = {
        'index': index,
        'category': category,
        # 'kinopoisk': api_ranked,
        'id_c': test_api.delay(),

        # api https://kinopoiskapiunofficial.tech
        # 'kinopoisk': response.json()['ratingKinopoisk'], # получаем рейтинг кинопоиска
        # 'imdb': response.json()['ratingImdb'], # получаем рейтин Imdb
    }

    return render(request, 'cinema/index.html', data)


def movie(request, slug, slug_video):
    # video model + category models detail
    video = Video.objects.select_related('cat').get(slug=slug_video)
    category = get_object_or_404(Category, slug=slug)
    video_list = Video.objects.select_related('cat').filter(cat=category)

    # views checker
    MovieService.view_check(video)
    # format: example - 1 223 324
    video.formatted_view = intcomma(video.view)
    video.save()

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
    comment_len = len(comment_list)

    # reviews quantity
    comment_success = Comment.objects.select_related('video_c').filter(type_r='Положительная').filter(video_c=video).values('type_r')
    comment_danger = Comment.objects.select_related('video_c').filter(type_r='Отрицательная').filter(video_c=video).values('type_r')

    # filters
    filter_success = request.GET.get('filter-success', '')
    filter_danger = request.GET.get('filter-danger', '')

    if filter_success:
        comment_list = Comment.objects.filter(video_c=video).select_related('video_c').filter(type_r='Положительная')
        comment_len = len(Comment.objects.filter(video_c=video).select_related('video_c').filter(type_r='Положительная'))

    if filter_danger:
        comment_list = Comment.objects.filter(video_c=video).select_related('video_c').filter(type_r='Отрицательная')
        comment_len = len(Comment.objects.filter(video_c=video).select_related('video_c').filter(type_r='Отрицательная'))

    data = {
        'video': video,
        'video_list': video_list,
        'cat': category,
        'form': form,
        'ranked': MovieService.points(comment_success, comment_danger), # import services

        # comment info and list
        'comment_success': comment_success,
        'comment_danger': comment_danger,
        'comment_list': comment_list,
        'comment_len': comment_len,
    }

    return render(request, 'cinema/movie.html', data)
