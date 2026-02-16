from dataclasses import asdict


class ToDictMixin:
    def to_dict(self):
        return asdict(self)


class FromDictMixin:
    @classmethod
    def from_dict(cls, data: dict):
        return cls(**data)