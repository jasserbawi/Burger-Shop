# implement the classes listed below
class FoodItem:

    # constructor
    def __init__(self, name, itemType, price):
        self.itemName = name
        self.foodType = itemType
        self.price = float(price)

    # common methods
    def getItemName(self):
        return self.itemName

    def getPrice(self):
        return self.price

    def getItemType(self):
        return self.foodType

    # implementing the item classes from the FoodItem class


class Burger(FoodItem):

    def __init__(self, name, itemType, price, toppings, size, sauce):
        super().__init__(name, itemType, price)

        self.toppings = toppings
        self.size = size
        self.sauce = sauce

    def getSize(self):
        return self.size


class Drink(FoodItem):

    def __init__(self, name, itemType, price, size):
        super().__init__(name, itemType, price)

        self.size = size


class Side(FoodItem):

    def __init__(self, name, itemType, price, quantity):
        super().__init__(name, itemType, price)

        self.quantity = quantity


class Combo(FoodItem):

    def __init__(self, burger, drink, sides):
        self.comboBurger = burger
        self.comboDrink = drink
        self.comboSides = sides

        self.totalPrice = self.comboBurger.getPrice() + self.comboDrink.getPrice() + self.comboSides.getPrice()

        super().__init__("Combo", "Combo", self.totalPrice)


class Order:

    def __init__(self, name):

        self.userName = name

        self.orderedItems = []  # this list stores the ordered items

    def add(self, item):
        # this method adds new item in ordered items list
        self.orderedItems.append(item)

    def orderTotal(self):
        # this method is used to calculate the total price of all items in the orderedItems list
        total = 0

        for item in self.orderedItems:
            total += item.getPrice()

        return total

    def printOrderedItems(self):

        print("\nUser name: ", self.userName)
        print("\n{:<20} {:<20} {:<20} {:<20}".format("Order No. ", "Item Name", "Item type", "Price"))

        count = 1
        for item in self.orderedItems:
            print(
                "\n{:<20} {:<20} {:<20} {:<20}".format(count, item.getItemName(), item.getItemType(), item.getPrice()))

        # following methods used to create a food item object by taking inputs from the user


def user_input_burger():
    # ask user for input and store it in burger object
    name = input("\nEnter burger name: ")
    burgerType = input("Enter burger type: ")
    price = input("Enter burger price: ")

    toppings = list(map(str, input("Enter all toppings you want on the burger separated by spaces: ").split(" ")))
    size = input("Enter burger size[small/large] : ")
    sauce = input("Enter burger sauce: ")

    b = Burger(name, burgerType, price, toppings, size, sauce)
    return b


def user_input_drink():
    # ask user for input and store it in drink object
    name = input("\nEnter drink name: ")
    drinkType = input("Enter drink type: ")
    price = input("Enter drink price: ")

    size = input("Enter the drink size in litres [1 Ltr/1.5 Ltr/2.50 Ltr]: ")

    d = Drink(name, drinkType, price, size)

    return d


def user_input_side():
    # ask user for input and store it in side object
    name = input("\nEnter sides name [fries/onion rings/garden salad]: ")
    sidesType = input("Enter sides type: ")
    price = input("Enter sides price: ")

    quantity = input("Enter the quantity of the sides: ")
    s = Side(name, sidesType, price, quantity)
    return s


def user_input_combo():
    print("\na combo includes one burger, one side, and one drink")
    c = Combo(user_input_burger(), user_input_drink(), user_input_side())
    # ask user for input and store it in combo object
    # a combo must include one burger, one side, and one drink
    return c


def take_order():
    userName = input("\nPlease enter your name: ")

    myOrder = Order(userName)

    while True:
        print("\nMenu: \n1. Burger \n2. Drink \n3. Side \n4. Combo \n5. Order")

        userChoice = input("\nEnter your choice from above: ")

        if userChoice == "1":

            myOrder.add(user_input_burger())

        elif userChoice == "2":

            myOrder.add(user_input_drink())

        elif userChoice == "3":

            myOrder.add(user_input_side())

        elif userChoice == "4":

            myOrder.add(user_input_combo())

        elif userChoice == "5":
            break

        else:
            print("Please select a valid choice")

    print("\nYour ordered Items are: ")
    myOrder.printOrderedItems()

    isOrder = input("\n1 for confirm order or 0 for cancel order: ")

    if isOrder == "1":

        print(f"\nOrder confirmed for the selected items!!!\n\nTotal pay: ${myOrder.orderTotal()}\n")

    elif isOrder == "0":

        print(f"\nOrder cancelled for the selected items!!!\n")

    else:
        print("\nInvalid selection, try again!!!")
        take_order()

    # display a thank you message
    print(f"\nThank you for your order!!\n")


print("Welcome to Burger Shop")
take_order()