import allure
import requests
import data
import generators
from conftest import create_user


class TestLoginUser:
    @allure.title('Вход под существующим пользователем. ')
    def test_login_for_existing_user(self, create_user):
        login = requests.post(f'{data.Url.LOGIN_URl}', json=create_user[1])
        login_json = login.json()
        assert (login_json['success'] == True and
                'accessToken' in login_json and
                'refreshToken' in login_json and
                login_json['user'] == {'email': create_user[0]['email'], 'name': create_user[0]['name']})

    @allure.title('Вход с неверным email. ')
    def test_login_for_invalid_email(self, create_user):
        login_data = {'email': generators.email_generator(), 'password': create_user[1]['password']}
        login = requests.post(f'{data.Url.LOGIN_URl}', json=login_data)
        assert login.status_code == 401 and login.json() == data.ResponseBody.LOGIN_USER_FOR_INVALID_FIELD

    @allure.title('Вход с неверным паролем. ')
    def test_login_for_invalid_password(self, create_user):
        login_data = {'email': create_user[1]['email'],'password': generators.password_generator()}
        login = requests.post(f'{data.Url.LOGIN_URl}', json=login_data)
        assert login.status_code == 401 and login.json() == data.ResponseBody.LOGIN_USER_FOR_INVALID_FIELD