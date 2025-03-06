#Name:
#Class: 5th Hour
#Assignment: HW22

#1. Create a class containing a def function that inits self and 3 other attributes for store items (stock, cost, and weight).
class Store:
    def __init__(self, stock, cost, weight):
        self.stock = stock
        self.cost = cost
        self.weight = weight

    def twice(self):
        self.cost *= 2






#2. Make 3 objects to serve as your store items and give them values to those 3 attributes defined in the class.
cheetos_puff = Store(10, 5, 12)
coke = Store(12, 6, 20)
potato_chips = Store(16, 6, 10)
#3. Print the stock of all three objects and the cost of the second store item.
print(f"Cheetos_puff stock {cheetos_puff.stock}")
print(f"coke cost {coke.cost} and stock {coke.stock}")
print(f"Potato chips stock {potato_chips.stock}")

#4. Make a def function within the class that doubles the cost an item, double the cost of the second store item, and print the new cost below the original cost print statement.


coke.twice()
print(f"coke price has double to {coke.cost}")

#5. Directly change the stock of the third store item to approx. 1/4th the original stock and then print the new stock amount.
potato_chips.stock = 4
print(f"New potato_chips stock changed to {potato_chips.stock}")

#6. Delete the first store item and then attempt to print the weight of the first store item. Create a try/except catch to fix the error.
del cheetos_puff
try:
    print(cheetos_puff.weight)
except:
    print("There is no cheetos in stock")


