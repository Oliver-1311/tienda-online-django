from typing import Type, TypeVar, Generic
from django.db import models
from src.application.repositories.base import IBaseRepository

T = TypeVar('T', bound=models.Model)

class BaseRepository(IBaseRepository, Generic[T]):
    def __init__(self, model: Type[T]):
        self.model = model

    def save(self, entity: T) -> T:
        entity.save()
        return entity

    def get(self, entity_id: int) -> T:
        return self.model.objects.get(id=entity_id)

    def delete(self, entity_id: int):
        self.model.objects.filter(id=entity_id).delete()

    def update(self, entity_id: int, **kwargs) -> T:
        entity = self.model.objects.filter(id=entity_id).update(**kwargs)
        return self.model.objects.get(id=entity_id)