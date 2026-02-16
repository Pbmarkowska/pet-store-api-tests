import json
from http import HTTPStatus


class StoreAssertions:
    def __init__(self, response):
        self.response = response
        self._data = None

    @property
    def data(self):
        if self._data is None:
            try:
                self._data = json.loads(self.response.content.decode('utf-8'))
            except json.JSONDecodeError:
                raise AssertionError(
                    f'Response is not valid JSON\n'
                    f'Status code: {self.response.status_code}\n'
                    f'Body: {self.response.content[:300]}'
                )
        return self._data

    def assert_store_inventory(self):
        assert self.response.status_code == HTTPStatus.OK