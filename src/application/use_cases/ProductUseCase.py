from src.application.repositories import IProductRepository

class ProductUseCase:

    def __init__(self, productRepository: IProductRepository):
        self.productRepository = productRepository

    def detail(self) -> str:
        data = self.productRepository.get(1)
        return data.name