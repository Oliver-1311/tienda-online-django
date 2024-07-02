from src.infrastructure.persistence.models import Product
from src.infrastructure.repositories.base import BaseRepository
from src.application.repositories import IProductRepository

class ProductRepository(IProductRepository, BaseRepository[Product]):

    def __init__(self):
        super().__init__(Product)

    def get_custom(self):
        return "Esto es personalizado"