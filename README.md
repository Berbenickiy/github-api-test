Сначала необходимо склонировать репозиторий с GitHub на ваш локальный компьютер.

Откройте терминал или командную строку.

Перейдите в директорию, куда хотите клонировать проект.
cd путь/до/вашей/папки 
git clone https://github.com/ваш_пользователь/github-api-test.git 
Замените "ваш_пользователь" на ваше имя пользователя на GitHub

Перейдите в директорию проекта: 
cd github-api-test

Создайте и Активируйте Виртуальное Окружение Windows PowerShell 
-m venv venv 
venv\Scripts\activate

Установите Зависимости 
pip install -r requirements.txt

Создание Файла .env
В корневой директории проекта уже есть файл-шаблон .env.example. 
Вам необходимо создать файл .env на его основе.
Для Windows:
copy .env.example .env

Заполнение Файла .env
Откройте файл .env в любом текстовом редакторе и заполните необходимые поля.

GITHUB_USERNAME=ваше_имя_пользователя
GITHUB_TOKEN=ваш_персональный_токен
REPO_NAME=имя_репозитория_для_теста

Запустите Тест 
python test_api.py

Тест
-создаёт
-проверяет
-удаляет репозиторий на GitHub.

