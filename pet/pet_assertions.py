import json
from http import HTTPStatus

from pygments.lexers import data


class PetAssertions:
    def __init__(self, response):
        self.response = response
        self._data = None

    @property
    def data(self):
        if self.data is None:
            try:
                self._data = json.loads(self.response.content.decode('utf-8'))
            except json.decoder.JSONDecodeError:
                raise AssertionError(
                    f'Response is not valid JSON\n'
                    f'Status code: {self.response.status_code}\n'
                    f'Body: {self.response.content[:300]}'
                )

    def assert_pet_added(self):
        assert self.response.status_code == HTTPStatus.OK