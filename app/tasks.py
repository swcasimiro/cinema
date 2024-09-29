from celery import Celery
import requests

url = "https://kinopoiskapiunofficial.tech/api/v2.2/films/1186526"
api = {'X-API-KEY': 'f98a5461-d00d-4929-9a5c-e441318daba7'}

app = Celery('example', broker='your_broker_url_here')


@app.task(bind=True, max_retries=2, default_retry_delay=3600)
def api_ranked(api, url):
    response = requests.get(url, headers=api)

    if response.status_code == 200:
        response = requests.get(url, headers=api)
    else:
        response = 'Недоступно'

    data = {
        'kinopoisk': response.json()['ratingKinopoisk'],  # получаем рейтинг кинопоиска
        'imdb': response.json()['ratingImdb'],  # получаем рейтин Imdb
    }