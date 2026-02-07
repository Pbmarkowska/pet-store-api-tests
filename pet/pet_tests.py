from pet.pet_assertions import PetAssertions
from pet.pet_methods import PetMethods
from pet.pet_models import Pet, Category, Tags


class TestPets:
    def test_add_pet(self):
        pet = Pet(name='doggie', category=Category(name="dogs"), photoUrls=['url'], tags=[Tags(name="friendly")])
        response = PetMethods.add_pet_to_store_inventory(pet)
        PetAssertions(response).assert_pet_added()
