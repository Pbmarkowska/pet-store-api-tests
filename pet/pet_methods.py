from dataclasses import asdict

import requests

from endpoints import PET, FIND_PET_BY_STATUS
from pet.pet_models import Pet


class PetMethods:
    @staticmethod
    def add_pet_to_store_inventory(pet: Pet):
        response = requests.post(f'{PET}', json=asdict(pet))
        return response

    @staticmethod
    def update_pet(data):
        response = requests.put(f'{PET}', json=data)
        return response

    @staticmethod
    def find_pet_by_status(status):
        response = requests.get(f'{FIND_PET_BY_STATUS}', params={'status': status})
        return response

    @staticmethod
    def find_pet_by_id(pet_id):
        response = requests.get(f'{FIND_PET_BY_STATUS}/{pet_id}')
        return response

    @staticmethod
    def update_pet_by_id(pet_id, data):
        response = requests.post(f'{PET}/{pet_id}', data={data})
        return response

    @staticmethod
    def delete_pet(pet_id):
        response = requests.delete(f'{PET}/{pet_id}')
        return response