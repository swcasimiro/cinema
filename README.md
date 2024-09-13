# cinema
<img src="https://img.shields.io/badge/django 5.2-black?style=for-the-badge&logo=django&logoColor=white" alt="Django Badge"/> 
<p>Веб-приложение для просмотра сериалов / фильмов онлайн. Сайт предоставляет готовый шаблон для создания своего онлайн-кинотеатра. Гибкий интерфейс, позволяющий заполнить сайт любым рода контента для просмотра.
Гибкое подключенное API позволяющее узнавать рейтинг в популярных онлайн-кинотеатрах для любого фильма. Возможность делиться своим мнение о просмотренной серии сериала.</p>


<strong><p>Используемые технологии:</p></strong>
  <p>Все использованные инструменты, которые были задействованы в реализации данного проекта.</p>
<div>
<p><code>Языки программирования</code></p>
  <a>
    <img src="https://img.shields.io/badge/python-346c99?style=for-the-badge&logo=python&logoColor=fecd3a" alt="Python Badge"/>
    <img src="https://img.shields.io/badge/javascript-black?style=for-the-badge&logo=javascript&logoColor=f6e019" alt="JavaScript Badge"/>
  </a>
<br>
<br>  
<p><code>Фреймворк и библиотеки</code></p>

<a>
    <img src="https://img.shields.io/badge/django-%23092E20.svg?style=for-the-badge&logo=django&logoColor=white" alt="Django Badge"/>
</a>
<br>
<br>
<p><code>База данных</code></p>
<a>
  <img src="https://img.shields.io/badge/postgresql-316093?style=for-the-badge&logo=postgresql&logoColor=white" alt="PostgreSQL Badge"/>
</a>
<a>
    <img src="https://img.shields.io/badge/sqlite-3f9cd8?style=for-the-badge&logo=sqlite&logoColor=white" alt="nginx Badge"/>
</a>

</div>

<br>

<strong><p>Настройка API для показа рейтинга:</p></strong>

<p>Для корректного отображения рейтинга нужно зарегестрироваться на сайте <a href="https://kinopoiskapiunofficial.tech/">Kinopoisk API Unofficial.
</a> В личном кабинете получить свой ключ. Далее в настройках проекта указать его по маршрутку <strong>cinema/views.py</strong> в переменной 
<code>appid = {'X-API-KEY': 'your_key'}</code>. Далее указать в переменной <code>base_url</code> ендпоинт. После выполнения всех этих действий
рейтинг обновится. Будьте аккуратне с использованием API и действуйте строго по инструкции.</p>

<br>
<strong><p>Настройка главной страницы:</p></strong>
<p>В базе данных создана модель главная страница. С помощью её вы можете заполнить <strong>index.html</strong>. Не стоит создавать больше одной модели, могут возникнуть
конфликты и страница будет отображена некорректно. В django-admin все поля детально расписаны.</p>

<br>

<strong><p>Активация проекта:</p></strong>
<code>venv\Scripts\activate.bat</code>
<br>
<br>
<code>pip install -r requirements.txt</code>
<br>
<br>
<code>python manage.py makemigrations</code>
<br>
<br>
<code>python manage.py migrate</code>
<br>
<br>
<code>python manage.py createsuperuser</code>
<br>
<br>

<strong><p>Инструкция при первом запуске:</p></strong>
<p>Перед использованием административной панели и создание новый суперюзеров. Ознакомьтесь с инструкцией ниже. Пользователь создан с которым вы можете перейти на следующий этап. А именно заполнению
самого сайта нужным вам контентом.</p>
<ul>
<li>База данных заполнена.</li>
<li>Произведены миграции</li>
<li>Создан superuser
<ul>
<li>Login: root</li>
<li>Password: 123</li>
</ul></li>
<li>Заполнены только несколько серий сериала "Черное лето".</li>
</ul>

<br>
<strong><p>Адреса для входа в административную панель:</p></strong>
<ul>
<li>http://127.0.0.1:8000/admin/</li>
<li>http://localhost/admin/</li>
<li><code>http://domain_name.ru/admin/</code></li>
</ul>
