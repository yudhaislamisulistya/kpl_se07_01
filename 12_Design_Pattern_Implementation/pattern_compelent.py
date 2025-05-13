from abc import ABC, abstractmethod


# Product - Interface yang mendefinisikan produk
class Product(ABC):
    @abstractmethod
    def use(self):
        pass


# ConcreteProduct - Implementasi nyata dari produk
class ConcreteProduct(Product):
    def use(self):
        print("Using Concrete Product!")


# ProductFactory - Kelas abstrak untuk pembuatan produk
class ProductFactory(ABC):
    @abstractmethod
    def create_product(self) -> Product:
        pass


# ConcreteProductFactory - Implementasi konkret dari Factory Method
class ConcreteProductFactory(ProductFactory):
    def create_product(self) -> Product:
        return ConcreteProduct()


# DisposalMethod - Kelas untuk mengelola penghancuran produk
class DisposalMethod:
    @staticmethod
    def dispose(product: Product):
        # Di sini kita hanya menghapus referensi objek dengan `del`, 
        # karena Python otomatis mengelola memori melalui garbage collection.
        del product
        print("Product disposed!")


# Penggunaan
if __name__ == "__main__":
    # Menggunakan Factory Method untuk membuat objek
    factory = ConcreteProductFactory()
    product = factory.create_product()
    
    # Menggunakan produk
    product.use()
    
    # Menggunakan Disposal Method untuk membersihkan produk setelah digunakan
    DisposalMethod.dispose(product)