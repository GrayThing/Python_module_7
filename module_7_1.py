class Product():

    def __init__(self, name, weight, category):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return f"'{self.name}', '{self.weight}', '{self.category}'"


class Shop():
    __file_name = 'products.txt'

    def get_products(self):
        file = open(self.__file_name, 'r')
        products = file.read()
        file.close()
        return products

    def write_file(self, text):
        file = open(self.__file_name, 'a')
        file.write(f'{text}\n')
        file.close()

    def add(self, *products: Product):
        products_str = self.get_products()
        for product in products:
            if product.name in products_str:
                print(f'Продукт {product.name} уже есть в магазине')
            else:
                self.write_file(f'Название: {product.name}, Вес: {product.weight}, Категория: {product.category}')



s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2) # __str__

s1.add(p1, p2, p3)

print(s1.get_products())