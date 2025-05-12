# Inventory Management System

## Overview

This project implements an **Inventory Management System** using Object-Oriented Programming (OOP) concepts in Python. The system is designed to handle various types of products such as **Electronics**, **Groceries**, and **Clothing**. It provides functionalities to manage stock, sales, and product information.

## Structure

### 1. Abstract Base Class: `Product`

The `Product` class serves as an abstract base class for all product types. It defines the common attributes and methods for handling products:

* **Attributes:**

  * `_product_id`: Unique identifier for the product
  * `_name`: Name of the product
  * `_price`: Price of the product
  * `_quantity_in_stock`: Quantity available in stock

* **Methods:**

  * `restock(amount)`: Restocks a given amount to the product's quantity.
  * `sell(quantity)`: Sells a given quantity of the product.
  * `get_total_value()`: Returns the total value of the product (price \* stock).
  * `__str__()`: Abstract method that is overridden in subclasses to return a string representation of the product.

### 2. Subclasses of `Product`

#### `Electronics`

* Attributes: `warranty_years`, `brand`
* Inherits from `Product` and adds specific attributes for electronics products.
* `__str__()` method returns formatted details including warranty and brand.

#### `Grocery`

* Attributes: `expiry_date`
* Inherits from `Product` and adds an expiry date attribute.
* `is_expired()` method checks if the product is expired.
* `__str__()` method returns formatted details including expiry information.

#### `Clothing`

* Attributes: `size`, `material`
* Inherits from `Product` and adds attributes specific to clothing.
* `__str__()` method returns formatted details including size and material.

### 3. `Inventory` Class

The `Inventory` class manages a collection of products and provides methods to manipulate the inventory.

* **Attributes:**

  * `_products`: A dictionary to store products where the key is the product ID and the value is the product object.

* **Methods:**

  * `add_product(product)`: Adds a new product to the inventory.
  * `remove_product(product_id)`: Removes a product from the inventory by its ID.
  * `search_by_name(name)`: Searches for products by name.
  * `search_by_type(product_type)`: Searches for products by type (Electronics, Grocery, etc.).
  * `list_all_products()`: Lists all products in the inventory.
  * `sell_product(product_id, quantity)`: Sells a given quantity of a product.
  * `restock_product(product_id, quantity)`: Restocks a product by a specified quantity.
  * `total_inventory_value()`: Calculates the total value of the inventory.
  * `remove_expired_products()`: Removes expired grocery items from the inventory.

## Requirements

To run this project, Python 3.x is required.

   ```bash
   python inventory_system.py
   ```

### Expected Output

```text
Electronics[ID: E001, Name: Laptop, Brand: Dell, Price: 1500.0, Stock: 5, Warranty: 2 years]
Electronics[ID: E002, Name: Computer, Brand: Dell, Price: 1200.0, Stock: 12, Warranty: 2 years]
Grocery[ID: G001, Name: Milk, Price: 2.5, Stock: 10, Expiry Date: 2025-01-01, Expired: False]
Clothing[ID: C001, Name: T-Shirt, Size: L, Material: Cotton, Price: 20.0, Stock: 15]
Total Inventory Value: 25750.0
```

## Conclusion

This system provides a simple yet effective inventory management solution using Python's OOP principles. It allows you to manage a variety of products, track stock levels, and calculate inventory values. The design is modular, making it easy to add new product types or inventory operations as needed.
