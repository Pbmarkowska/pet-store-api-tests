from dataclasses import asdict

import requests

from endpoints import USER
from models.user_models import User


class UserMethods:
    @staticmethod
    def add_user(user: User):
        response = requests.post(f'{USER}', json=asdict(user))
        return response

    @staticmethod
    def get_user_by_username(username: str):
        response = requests.get(f'{USER}/{username}')
        return response

    @staticmethod
    def update_user(user: User):
        response = requests.put(f'{USER}', json=asdict(user))
        return response

    @staticmethod
    def delete_user(username: str):
        response = requests.delete(f'{USER}/{username}')
        return response

    @staticmethod
    def user_login(username, password):
        response = requests.get(f'{USER}/login', params={'username': username, 'password': password})
        return response

    @staticmethod
    def user_logout():
        response = requests.get(f'{USER}/logout')
        return response