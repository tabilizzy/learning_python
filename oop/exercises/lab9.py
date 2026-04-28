'''
**Lab 2: Market Stall Inventory System**
**Real-world challenge**: You run a small provision store in Douala market. You need to track products, prices, stock, and sales. Prevent selling items you don’t have.

**Objectives**:
- Use dictionaries and sets
- Class with properties
- Loops to process collections

**Requirements**:
1. Create a Product class:
__init__ with name (str), price (float), stock (int)
2. Make stock a private attribute with setter (stock cannot go below 0)
3. Method sell(quantity) → reduces stock and returns total price

**Main program**:
- Use a dict where key = product name, value = Product object
- Use a set to keep track of low-stock items (stock < 5)

**Menu**:
1. Add new product
2. Sell product (ask name and quantity)
3. Show all products
4. Show low-stock items
5. Exit

- Use for loops to display products nicely
- Error handling: invalid quantity, product not found

**Test challenge**:
Add “Rice” (price 500, stock 10), “Oil” (price 1200, stock 3). Sell 6 Rice → stock becomes 4. Sell 4 Oil → stock 0 and it should appear in low-stock set.
'''
class Product:
    def __init__(self, name: str, price: float, stock: int):
        self.name = name
        self.price = price
        self.__stock = 0
        self.stock = stock  # use setter

    # Getter
    def stock(self):
        return self.__stock

    # Setter (validation: stock cannot go below 0)
    def stock(self, value):
        if value <= 0:
            raise ValueError("Stock cannot be negative!")
        self.__stock = value

    # Sell method
    def sell(self, quantity):
        if quantity <= 0:
            raise ValueError("Quantity must be positive!")
        if quantity > self.__stock:
            raise ValueError("Not enough stock available!")
        
        self.__stock -= quantity
        return quantity * self.price

    def __str__(self):
        return f"{self.name} | Price: {self.price} | Stock: {self.stock}"


products = {}  # dictionary: name -> Product
low_stock = set()  # set of product names


def update_low_stock():
    low_stock.clear()
    for name, product in products.items():
        if product.stock < 5:
            low_stock.add(name)


def add_product():
    name = input("Enter product name: ")
    price = float(input("Enter price: "))
    stock = int(input("Enter stock: "))
    if name in products:
        print("Product already exists!")
        return
    products[name] = Product(name, price, stock)
    update_low_stock()
    print("Product added successfully!")



def sell_product():
    name = input("Enter product name: ")
    if name not in products:
        print("Product not found!")
        return
    quantity = int(input("Enter quantity to sell: "))
    total = products[name].sell(quantity)
    update_low_stock()
    print(f"Sold! Total price: {total}")

def show_products():
    if not products:
        print("No products available.")
        return

    print("\n--- Product List ---")
    for product in products.values():
        print(product)


def show_low_stock():
    if not low_stock:
        print("No low-stock items.")
        return

    print("\n--- Low Stock Items ---")
    for name in low_stock:
        print(name)



# Menu Loop

print("***************************************************")
print("Welcome To Our Market Stall Inventory System ")
print("***************************************************")
while True:
    print("""
    1. Add new product
    2. Sell product
    3. Show all products
    4. Show low-stock items
    5. Exit
            """)

    choice = int(input("Choose an option: "))

    match choice:
        case 1:
            add_product()
        case 2:
            sell_product()
        case 3:
            show_products()
        case 4:
            show_low_stock()
        case 5:
            print("Thank you for you for shopping with us, have a great day")
            break
        case _:
            print("Invalid selection")



