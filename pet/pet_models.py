from dataclasses import dataclass, field
from typing import Optional, List


@dataclass
class Category:
    id: Optional[int] = None
    name: str = ""

@dataclass
class Tags:
    id: Optional[int] = None
    name: str = None

@dataclass
class Pet:
    name: str
    photoUrls: List[str] = field(default_factory=list)
    category: Optional[Category] = field(default_factory=Category)
    tags: List[Tags] = field(default_factory=list)
    status: str = "available"
    id: Optional[int] = None

