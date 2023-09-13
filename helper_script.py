import os
import requests
from urllib.parse import urlparse


def get_picture_format(url):
    picture_parse = urlparse(url)
    path = picture_parse.path
    return os.path.splitext(path)[1]


def download_picture(link, params, path, filename):
    response = requests.get(link, params=params)
    response.raise_for_status()
    with open(f"{path}/{filename}", 'wb') as file:
        file.write(response.content)


def send_picture(bot, path, file, chat_id):
    with open(f"{path}/{file}", "rb") as file: 
        bot.send_photo(chat_id=chat_id, photo=file)
