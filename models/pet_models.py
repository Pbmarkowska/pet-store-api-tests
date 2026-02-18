from dataclasses import dataclass, field
from typing import Optional, List

from utils.mixins import ToDictMixin, FromDictMixin


@dataclass
class Category:
    id: Optional[int] = None
    name: str = ""

@dataclass
class Tags:
    id: Optional[int] = None
    name: str = None

@dataclass
class Pet(ToDictMixin, FromDictMixin):
    name: str
    photoUrls: List[str] = field(default_factory=list)
    category: Optional[Category] = field(default_factory=Category)
    tags: List[Tags] = field(default_factory=list)
    status: str = "available"
    id: Optional[int] = None

    @classmethod
    def from_dict(cls, data: dict):
        return cls(
            id=data["id"],
            name=data["name"],
            category=Category(**data["category"]),
            photoUrls=data.get("photoUrls", []),
            tags=[Tags(**tag) for tag in data.get("tags", [])],
            status=data.get("status")
        )
