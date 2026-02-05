import requests

from pet_store_api_tests.endpoints import STORE_INVENTORY


class StoreMethods:
    @staticmethod
    def get_store_inventory():
        response = requests.get(f'{STORE_INVENTORY}')
        return response