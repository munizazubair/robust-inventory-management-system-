from abc import ABC, abstractmethod
from datetime import date

# 1. Abstract Base Class: Product
class Product(ABC):
    def __init__(self, product_id, name, price, quantity_in_stock):
        self._product_id = product_id
        self._name = name
        self._price = price
        self._quantity_in_stock = quantity_in_stock

    @abstractmethod
    def __str__(self):
        pass

    def restock(self, amount):
        self._quantity_in_stock += amount

    def sell(self, quantity):
        if quantity > self._quantity_in_stock:
            raise ValueError("Not enough stock to sell.")
        self._quantity_in_stock -= quantity

    def get_total_value(self):
        return self._price * self._quantity_in_stock

    def get_product_id(self):
        return self._product_id

    def get_name(self):
        return self._name

    def get_quantity(self):
        return self._quantity_in_stock

    def get_type(self):
        return self.__class__.__name__


# 2. Subclasses

class Electronics(Product):
    def __init__(self, product_id, name, price, quantity_in_stock, warranty_years, brand):
        super().__init__(product_id, name, price, quantity_in_stock)
        self.warranty_years = warranty_years
        self.brand = brand

    def __str__(self):
        return (f"Electronics[ID: {self._product_id}, Name: {self._name}, Brand: {self.brand}, "
                f"Price: {self._price}, Stock: {self._quantity_in_stock}, "
                f"Warranty: {self.warranty_years} years]")


class Grocery(Product):
    def __init__(self, product_id, name, price, quantity_in_stock, expiry_date):
        super().__init__(product_id, name, price, quantity_in_stock)
        self.expiry_date = expiry_date 

    def is_expired(self):
        return date.today() > self.expiry_date

    def __str__(self):
        return (f"Grocery[ID: {self._product_id}, Name: {self._name}, Price: {self._price}, "
                f"Stock: {self._quantity_in_stock}, Expiry Date: {self.expiry_date}, "
                f"Expired: {self.is_expired()}]")


class Clothing(Product):
    def __init__(self, product_id, name, price, quantity_in_stock, size, material):
        super().__init__(product_id, name, price, quantity_in_stock)
        self.size = size
        self.material = material

    def __str__(self):
        return (f"Clothing[ID: {self._product_id}, Name: {self._name}, Size: {self.size}, "
                f"Material: {self.material}, Price: {self._price}, Stock: {self._quantity_in_stock}]")


# 3. Inventory Class
class Inventory:
    def __init__(self):
        self._products = {}

    def add_product(self, product):
        if product.get_product_id() in self._products:
            raise ValueError("Product with this ID already exists.")
        self._products[product.get_product_id()] = product

    def remove_product(self, product_id):
        if product_id in self._products:
            del self._products[product_id]

    def search_by_name(self, name):
        return [p for p in self._products.values() if p.get_name().lower() == name.lower()]

    def search_by_type(self, product_type):
        return [p for p in self._products.values() if p.get_type().lower() == product_type.lower()]

    def list_all_products(self):
        return [str(p) for p in self._products.values()]

    def sell_product(self, product_id, quantity):
        if product_id not in self._products:
            raise ValueError("Product ID not found.")
        self._products[product_id].sell(quantity)

    def restock_product(self, product_id, quantity):
        if product_id not in self._products:
            raise ValueError("Product ID not found.")
        self._products[product_id].restock(quantity)

    def total_inventory_value(self):
        return sum(p.get_total_value() for p in self._products.values())

    def remove_expired_products(self):
        to_remove = []
        for product_id, product in self._products.items():
            if isinstance(product, Grocery) and product.is_expired():
                to_remove.append(product_id)
        for product_id in to_remove:
            del self._products[product_id]

if __name__ == "__main__":
    inv = Inventory()

    # Add some products
    e1 = Electronics("E001", "Laptop", 1500.0, 5, 2, "Dell") #add in eletronics
    e2 = Electronics("E002", "Computer", 1200.0, 12, 2, "Dell") #add in electronics

    g1 = Grocery("G001", "Milk", 2.5, 10, date(2025, 1, 1)) #add in grocery
    c1 = Clothing("C001", "T-Shirt", 20.0, 15, "L", "Cotton") # add i clothing

    inv.add_product(e1)
    inv.add_product(e2)
    inv.add_product(g1)
    inv.add_product(c1)

    # List all
    for item in inv.list_all_products():
        print(item)

    # Sell a product
    inv.sell_product("C001", 5)

    # Check total value
    print("Total Inventory Value:", inv.total_inventory_value())

    # Remove expired items
    inv.remove_expired_products()
