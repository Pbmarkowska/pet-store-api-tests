import json
import os
from http import HTTPStatus

from pygments.lexers import data


class PetAssertions:
    def __init__(self, response):
        self.response = response
        self._data = None

    @property
    def data(self):
        if self._data is None:
            try:
                self._data = json.loads(self.response.content.decode('utf-8'))
            except json.decoder.JSONDecodeError:
                raise AssertionError(
                    f'Response is not valid JSON\n'
                    f'Status code: {self.response.status_code}\n'
                    f'Body: {self.response.content[:300]}'
                )
        return self._data

    def assert_pet_added(self):
        assert self.response.status_code == HTTPStatus.OK

    def assert_pet_image_added(self, image_path):
        expected_size = os.path.getsize(image_path)
        image_name = os.path.splitext(os.path.basename(image_path))[0]
        data = self.response.json()
        assert self.response.status_code == HTTPStatus.OK
        assert 'File uploaded to' in data["message"]
        assert str(expected_size) in data["message"]
        assert image_name in data["message"]

    def assert_pet_matches(self, expected_id: int, expected_name: str):
        assert self.response.status_code == HTTPStatus.OK, f'Expected status code: {HTTPStatus.OK}, but got {self.response.status_code}'
        assert self.data.get('id') == expected_id, f'Expected id: {expected_id}, but got {self.data["id"]}'
        assert self.data.get('name') == expected_name, f'Expected name: {expected_name}, but got {self.data["name"]}'
        return self

    def assert_pet_deleted(self):
        assert self.response.status_code == HTTPStatus.OK