from celery import Celery, shared_task
import requests

u = "https://kinopoiskapiunofficial.tech/api/v2.2/films/1186526"
a = {'X-API-KEY': 'f98a5461-d00d-4929-9a5c-e441318daba7'}

app = Celery('example', broker='redis://localhost:6379')


@app.task
def bar():
    return "Hello world"


@app.task(rata_limit='0/h')
def test_api():
    response = requests.get('http://127.0.0.1:8000/api/beta/comment/')

    id_c = response.json()
    print(id_c["id"])


# @app.task(bind=True, max_retries=2, default_retry_delay=3600, track_started=True)
@app.task(rate_limit='10/h')
def api_ranked():
    url = "https://kinopoiskapiunofficial.tech/api/v2.2/films/1186526"
    api = {'X-API-KEY': 'f98a5461-d00d-4929-9a5c-e441318daba7'}
    response = requests.get(url, headers=api)

    if response.status_code == 200:
        response = requests.get(url, headers=api)
    else:
        response = 'Недоступно'

    data = {
        'kinopoisk': response.json()['ratingKinopoisk'],  # получаем рейтинг кинопоиска
        'imdb': response.json()['ratingImdb'],  # получаем рейтин Imdb
    }

    kinopoisk = response.json()['ratingKinopoisk']

    return kinopoisk

@shared_task
def barsa():
    return "Hello world"