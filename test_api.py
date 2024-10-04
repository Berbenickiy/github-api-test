
import os
import sys
import requests
from dotenv import load_dotenv


def load_environment():
    load_dotenv()
    username = os.getenv('GITHUB_USERNAME')
    token = os.getenv('GITHUB_TOKEN')
    repo_name = os.getenv('REPO_NAME')

    if not all([username, token, repo_name]):
        print("Ошибка: Не все переменные окружения установлены.")
        sys.exit(1)

    return username, token, repo_name


def create_repo(username, token, repo_name):
    url = "https://api.github.com/user/repos"
    payload = {
        "name": repo_name,
        "description": "Тестовый репозиторий для автоматизированного теста",
        "private": False
    }
    response = requests.post(url, auth=(username, token), json=payload)
    if response.status_code == 201:
        print(f"Репозиторий '{repo_name}' успешно создан.")
    else:
        print(f"Ошибка при создании репозитория: {response.status_code}")
        print(response.json())
        sys.exit(1)


def check_repo_exists(username, token, repo_name):
    url = f"https://api.github.com/repos/{username}/{repo_name}"
    response = requests.get(url, auth=(username, token))
    if response.status_code == 200:
        print(f"Репозиторий '{repo_name}' подтверждён как существующий.")
    else:
        print(f"Репозиторий '{repo_name}' не найден.")
        sys.exit(1)


def delete_repo(username, token, repo_name):
    url = f"https://api.github.com/repos/{username}/{repo_name}"
    response = requests.delete(url, auth=(username, token))
    if response.status_code == 204:
        print(f"Репозиторий '{repo_name}' успешно удалён.")
    else:
        print(f"Ошибка при удалении репозитория: {response.status_code}")
        print(response.json())
        sys.exit(1)


def main():
    username, token, repo_name = load_environment()
    create_repo(username, token, repo_name)
    check_repo_exists(username, token, repo_name)
    delete_repo(username, token, repo_name)
    print("Автоматический тест завершён успешно.")


if __name__ == "__main__":
    main()

