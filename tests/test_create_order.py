import allure
import requests
import data
import generators
from conftest import create_user

class TestCreateOrder:
    @allure.title('Создание заказа без авторизации. ')
    def test_create_order_without_authorization_success(self):
        ingredients = requests.get(data.Url.GET_INGREDIENTS)
        request_body = {'ingredients': [ingredients.json()['data'][0]['_id']]}
        create_order = requests.post(data.Url.CREATE_ORDER, json=request_body)
        create_order_json = create_order.json()
        assert (create_order_json['success'] == True and
                'name' in create_order_json and
                'order' in  create_order_json and
                'number' in create_order_json['order'])

    @allure.title('Создание заказа с авторизацией. ')
    def test_create_order_with_authorization_success(self, create_user):
        ingredients = requests.get(data.Url.GET_INGREDIENTS)
        request_body = {'ingredients': [ingredients.json()['data'][0]['_id']]}
        headers = {'Authorization': create_user[2]}
        create_order = requests.post(data.Url.CREATE_ORDER, json=request_body, headers=headers)
        create_order_json = create_order.json()
        assert (create_order_json['success'] == True and
                'name' in create_order_json and
                'order' in create_order_json and
                'number' in create_order_json['order'])

    @allure.title('Создание заказа с ингредиентами. ')
    def test_create_order_with_ingredients_success(self):
        ingredients = requests.get(data.Url.GET_INGREDIENTS)
        request_body = {'ingredients': [ingredients.json()['data'][0]['_id'], ingredients.json()['data'][2]['_id']]}
        create_order = requests.post(data.Url.CREATE_ORDER, json=request_body)
        create_order_json = create_order.json()
        assert (create_order_json['success'] == True and
                'name' in create_order_json and
                'order' in create_order_json and
                'number' in create_order_json['order'])

    @allure.title('Создание заказа без ингредиентов. ')
    def test_create_order_without_ingredients_error(self):
        request_body = data.InvalidDataForOrderCreate.WITHOUT_INGREDIENTS
        create_order = requests.post(data.Url.CREATE_ORDER, json=request_body)
        assert create_order.status_code == 400 and create_order.json() == data.ResponseBody.CREATE_ORDER_WITHOUT_INGREDIENTS

    @allure.title('Создание заказа с неверным хешем ингредиента. ')
    def test_create_order_with_invalid_ingredients_error(self):
        request_body = data.InvalidDataForOrderCreate.INVALID_INGREDIENT
        create_order = requests.post(data.Url.CREATE_ORDER, json=request_body)
        assert create_order.status_code == 500