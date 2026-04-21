import allure

from assertions.user_assertions import UserAssertions
from methods.user_methods import UserMethods
from models.user_models import User
from utils.allure_utils import attach_response


class TestUsers:
    @allure.title("Create user - success")
    def test_create_user(self):
        user = User(id=1, username='test', firstName='first name', lastName='last name', password='password', email='test@example.com', phone='123', userStatus=1)
        response = UserMethods.add_user(user)
        attach_response(response)
        UserAssertions(response).assert_user_created()