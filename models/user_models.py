from dataclasses import dataclass

from utils.mixins import FromDictMixin, ToDictMixin


@dataclass
class User(ToDictMixin, FromDictMixin):
    id: int
    username: str
    firstName: str
    lastName: str
    email: str
    password: str
    phone: str
    userStatus: int