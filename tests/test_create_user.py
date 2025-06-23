import allure
import requests
import data
import pytest

class TestCreateUser:
    @allure.title('Создание уникального пользователя. ')
    def test_create_unique_user(self, generate_user_data):
        registration = requests.post(f'{data.Url.REGISTER_URL}', json=generate_user_data[0])
        registration_json = registration.json()
        assert (registration_json['success'] == True and
                'accessToken' in registration_json and
                'refreshToken' in registration_json and
                registration_json['user'] == {'email': generate_user_data[0]['email'], 'name': generate_user_data[0]['name']})

    @allure.title('Создание существующего пользователя. ')
    def test_create_duplicate_user(self, create_user):
        registration = requests.post(f'{data.Url.REGISTER_URL}', json=create_user[0])
        assert registration.status_code == 403 and registration.json() == data.ResponseBody.CREATE_DUPLICATE_USER

    @allure.title('Создание пользователя без одного из полей. ')
    @pytest.mark.parametrize('data_setup', data.InvalidDataForRegistration.data)
    def test_create_user_empty_field_error(self, data_setup):
        registration = requests.post(f'{data.Url.REGISTER_URL}', json=data_setup)
        assert registration.status_code == 403 and registration.json() == data.ResponseBody.CREATE_USER_FOR_EMPTY_FIELD
