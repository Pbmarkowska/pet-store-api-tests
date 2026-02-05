from http import HTTPStatus

import requests

from pet_store_api_tests.endpoints import STORE_INVENTORY


class TestStore:
    def test_get_store_inventory(self):
        response = requests.get(f'{STORE_INVENTORY}')
        assert response.status_code == HTTPStatus.OK

