from dataclasses import asdict
from pathlib import Path

import requests

from endpoints import PET, FIND_PET_BY_STATUS, UPLOAD_PET_IMAGE
from models.pet_models import Pet

class PetMethods:
    @staticmethod
    def add_pet_to_store_inventory(pet: Pet):
        response = requests.post(f'{PET}', json=asdict(pet))
        return response

    @staticmethod
    def add_pet_image(pet_id: int, image_path: Path):
        url = UPLOAD_PET_IMAGE.format(petId=pet_id)
        with open(image_path, "rb") as img_file:
            files = {"file": img_file}
            response = requests.post(url, headers={"accept": "application/json"}, files=files)

        return response

    @staticmethod
    def update_pet(pet: Pet):
        response = requests.put(f'{PET}', json=asdict(pet))
        return response

    @staticmethod
    def find_pet_by_status(status):
        response = requests.get(f'{FIND_PET_BY_STATUS}', params={'status': status})
        return response

    @staticmethod
    def find_pet_by_id(pet_id):
        response = requests.get(f'{PET}/{pet_id}')
        return response

    @staticmethod
    def update_pet_by_id(pet_id, pet: Pet):
        response = requests.post(f'{PET}/{pet_id}', data=asdict(pet))
        return response

    @staticmethod
    def delete_pet(pet_id):
        response = requests.delete(f'{PET}/{pet_id}')
        return response