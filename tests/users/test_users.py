from assertions.user_assertions import UserAssertions
from methods.user_methods import UserMethods
from models.user_models import User


class TestUsers:
    def test_create_user(self):
        user = User(id=1, username='test', firstName='first name', lastName='last name', password='password', email='test@example.com', phone='123', userStatus=1)
        response = UserMethods.add_user(user)
        UserAssertions(response).assert_user_created()