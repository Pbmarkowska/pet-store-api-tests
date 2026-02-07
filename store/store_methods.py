from dataclasses import asdict

import requests

from endpoints import STORE_INVENTORY, ORDER
from store.store_models import Order


class StoreMethods:
    @staticmethod
    def get_store_inventory():
        response = requests.get(f'{STORE_INVENTORY}')
        return response

    @staticmethod
    def get_order_by_id():
        response = requests.get(f'{ORDER}')
        return response

    @staticmethod
    def create_order(order: Order):
        response = requests.post(f'{ORDER}', json=asdict(order))
        return response

    @staticmethod
    def delete_order(order_id):
        response = requests.delete(f'{ORDER}/{order_id}')
        return response