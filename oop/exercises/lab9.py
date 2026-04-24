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

