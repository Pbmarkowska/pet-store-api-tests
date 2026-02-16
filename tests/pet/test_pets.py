from pathlib import Path

from assertions.pet_assertions import PetAssertions
from methods.pet_methods import PetMethods
from models.pet_models import Category, Pet, Tags


class TestPets:
    BASE_DIR = Path(__file__).resolve().parent.parent.parent
    PET_IMG_PATH = BASE_DIR / 'resources' / 'golden-retriever-tongue-out.jpg'

    def test_add_pet(self):
        pet = Pet(name='doggie', category=Category(name="dogs"), photoUrls=['url'], tags=[Tags(name="friendly")])
        response = PetMethods.add_pet_to_store_inventory(pet)
        PetAssertions(response).assert_pet_added()

    def test_add_pet_image(self):
        response = PetMethods.add_pet_image(pet_id=1, image_path=self.PET_IMG_PATH)
        PetAssertions(response).assert_pet_image_added(self.PET_IMG_PATH)

    def test_get_pet_by_id(self, add_pet_and_get_id_and_name_scope_function):
        pet_id, pet_name = add_pet_and_get_id_and_name_scope_function
        response = PetMethods.find_pet_by_id(pet_id=pet_id)
        PetAssertions(response).assert_pet_id_and_name_matches(pet_id, pet_name)

    def test_update_pet(self, add_pet_and_get_id_and_name_scope_function):
        pet_id, _ = add_pet_and_get_id_and_name_scope_function

        updated_pet = Pet(
            id=pet_id,
            name='andrzej',
            category=Category(id=2, name='dogs'),
            photoUrls=['https://example.com', 'https://example2.com'],
            tags=[
                Tags(id=1, name='not friendly'),
                Tags(id=2, name='small')
            ]
        )

        PetMethods.update_pet(updated_pet)
        response = PetMethods.find_pet_by_id(pet_id)

        PetAssertions(response).assert_pet_matches(updated_pet.to_dict())