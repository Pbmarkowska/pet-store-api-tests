from dataclasses import dataclass
from typing import Optional


@dataclass
class Order:
    id: Optional[int] = None
    petId: int = 0
    quantity: int = 1
    shipDate: Optional[str] = None
    status: str = 'placed'
    complete: bool = False
