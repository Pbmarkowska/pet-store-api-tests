
BASE_URL = 'https://petstore.swagger.io/v2'
STORE_INVENTORY = f'{BASE_URL}/store/inventory'
ORDER = f'{BASE_URL}{STORE_INVENTORY}/order'
USER = f'{BASE_URL}/user'
PET = f'{BASE_URL}/pet'
FIND_PET_BY_STATUS = f'{PET}/findByStatus'
UPLOAD_PET_IMAGE = f'{PET}/{{petId}}/uploadImage'