import pytest
import requests
from data import Url

import generators

@pytest.fixture
def generate_user_data():
    email = generators.email_generator()
    password = generators.password_generator()
    name = generators.name_generator()

    create_user_body = {'email': email, 'password': password, 'name': name}
    login_user_body = {'email': email, 'password': password}
    yield [create_user_body, login_user_body]

    login_user = requests.post(Url.LOGIN_URl, json=login_user_body)
    headers = {'Authorization': login_user.json()['accessToken']}
    requests.delete(Url.DELETE_URL, headers=headers)

@pytest.fixture
def create_user():
    email = generators.email_generator()
    password = generators.password_generator()
    name = generators.name_generator()

    create_user_body = {'email': email, 'password': password, 'name': name}
    login_user_body = {'email': email, 'password': password}
    registration = requests.post(f'{Url.REGISTER_URL}', json=create_user_body)
    yield [create_user_body, login_user_body, registration.json()['accessToken']]

    login_user = requests.post(Url.LOGIN_URl, json=login_user_body)
    headers = {'Authorization': login_user.json()['accessToken']}
    requests.delete(Url.DELETE_URL, headers=headers)