from abc import ABC, abstractmethod

class IBaseRepository(ABC):
    @abstractmethod
    def save(self, entity):
        pass

    @abstractmethod
    def get(self, entity_id: int):
        pass

    @abstractmethod
    def delete(self, entity_id: int):
        pass

    @abstractmethod
    def update(self, entity_id: int, **kwargs):
        pass