import uuid

import allure
import requests

import data

TIMEOUT = 30


def generate_user():
    suffix = uuid.uuid4().hex[:10]
    return {
        'email': f'julia_{suffix}@yandex.ru',
        'password': 'password',
        'name': 'Julia',
    }


@allure.step('Создать пользователя')
def register_user(payload):
    return requests.post(data.BASE_URL + data.REGISTER, json=payload, timeout=TIMEOUT)


@allure.step('Удалить пользователя')
def delete_user(token):
    return requests.delete(
        data.BASE_URL + data.USER,
        headers={'Authorization': token},
        timeout=TIMEOUT,
    )
