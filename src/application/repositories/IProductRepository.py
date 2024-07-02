from abc import abstractmethod
from src.application.repositories.base import IBaseRepository

class IProductRepository(IBaseRepository):

    @abstractmethod
    def get_custom(self):
        pass