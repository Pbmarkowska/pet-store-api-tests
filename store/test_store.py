import requests

from endpoints import STORE_INVENTORY
from store.store_assertions import StoreAssertions


class TestStore:
    def test_get_store_inventory(self):
        response = requests.get(f'{STORE_INVENTORY}')
        StoreAssertions(response).assert_store_inventory()

