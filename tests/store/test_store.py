import allure
import requests

from endpoints import STORE_INVENTORY
from assertions.store_assertions import StoreAssertions
from utils.allure_utils import attach_response


class TestStore:
    @allure.title("Get store inventory - success")
    def test_get_store_inventory(self):
        response = requests.get(f'{STORE_INVENTORY}')
        attach_response(response)
        StoreAssertions(response).assert_store_inventory()

