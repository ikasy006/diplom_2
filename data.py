import generators

class Url:
    MAIN_URL = 'https://stellarburgers.nomoreparties.site'
    LOGIN_URl = f'{MAIN_URL}/api/auth/login'
    REGISTER_URL = f'{MAIN_URL}/api/auth/register'
    DELETE_URL = f'{MAIN_URL}/api/auth/user'
    GET_INGREDIENTS = f'{MAIN_URL}/api/ingredients'
    CREATE_ORDER = f'{MAIN_URL}/api/orders'

class ResponseBody:
    CREATE_DUPLICATE_USER = {"success": False, "message": "User already exists"}
    CREATE_USER_FOR_EMPTY_FIELD = {"success": False, "message": "Email, password and name are required fields"}
    LOGIN_USER_FOR_INVALID_FIELD = { "success": False, "message": "email or password are incorrect"}
    CREATE_ORDER_WITHOUT_INGREDIENTS = {"success": False, "message": "Ingredient ids must be provided"}

class InvalidDataForRegistration:
    data = [
        {'email': generators.email_generator(),
         'name': generators.name_generator()},
        {'password': generators.password_generator(),
         'name': generators.name_generator()},
        {'email': generators.email_generator(),
         'password': generators.password_generator()}
    ]

class InvalidDataForOrderCreate:
    INVALID_INGREDIENT = {'ingredients': ['123456789']}
    WITHOUT_INGREDIENTS = {'ingredients': []}
