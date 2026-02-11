import random
from contextlib import contextmanager

import pytest

from pet.pet_assertions import PetAssertions
from pet.pet_methods import PetMethods
from pet.pet_models import Pet
from utils.utils import generate_pet_name


@contextmanager
def _add_pet_and_get_id_and_name():
    pet_id = random.randint(1, 100)

    pet_name = generate_pet_name(pet_id)

    pet = Pet(name=pet_name, id=pet_id)

    response = PetMethods.add_pet_to_store_inventory(pet)
    PetAssertions(response).assert_pet_added()

    try:
        yield pet_id, pet_name
    finally:
        response = PetMethods.delete_pet(pet_id)
        PetAssertions(response).assert_pet_deleted()

@pytest.fixture(scope='class')
def add_pet_and_get_id_and_name_scope_class():
    with _add_pet_and_get_id_and_name() as (pet_id, pet_name):
        yield pet_id, pet_name


@pytest.fixture(scope='function')
def add_pet_and_get_id_and_name_scope_function():
    with _add_pet_and_get_id_and_name() as (pet_id, pet_name):
        yield pet_id, pet_name
        
