# business logic

from dotenv import load_dotenv
import requests
import os
from .models import Video, Comment

load_dotenv()

# https://kinopoiskapiunofficial.tech API рейтинга
base_url = "https://kinopoiskapiunofficial.tech/api/v2.2/films/1186526"
appid = {'X-API-KEY': os.getenv('X-API-KEY')}

response = requests.get(base_url, headers=appid)


class MovieService:
    # вычисление рейтинга из моделей
    def points(success: list, danger: list) -> float:
        ranked = len(success)*5 + len(danger)
        len_comment = len(success) + len(danger)

        if len_comment:
            return float(f"{ranked / len_comment:.{1}f}")

        return 0.0

    def view_check(video):
        video.view = video.view + 1
        video.save()
