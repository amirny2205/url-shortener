In progress ...

Выполнение вот этого тестового: https://github.com/avito-tech/auto-backend-trainee-assignment

### запуск сервиса:
заполняем .env ; заполняем свои сеттинс в config/settings/*.py

запускаем (сначала миграции), затем сервер python manage.py runserver --settings=config.settings.dev

теперь отправляем POST на /shorten/ с параметрами redirect_to в фомате http://www.google.com и опционально shorten(любая строка). Нам возвращаются данные объекта ссылки.

затем переходим /{shorten} и нас перенаправляет куда надо.