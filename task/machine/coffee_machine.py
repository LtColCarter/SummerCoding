# Write your code here
class CoffeeMachine:
    def __init__(self, water, milk, beans, cups, money):
        self.water = water
        self.milk = milk
        self.beans = beans
        self.cups = cups
        self.money = money

    def remaining(self):
        print("The coffee machine has:")
        print(str(self.water) + " of water")
        print(str(self.milk) + " of milk")
        print(str(self.beans) + " of coffee beans")
        print(str(self.cups) + " of disposable cups")
        print("$" + str(self.money) + " of money")

    def buy(self, coffee_type):
        if coffee_type == "1":
            if self.water >= 250 and self.beans >= 16 and self.cups >= 1:
                self.money += 4
                self.water -= 250
                self.beans -= 16
                self.cups -= 1
                print("I have enough resources, making you a coffee!")
            else:
                if self.water < 250:
                    print("Sorry, not enough water!")
                elif self.beans < 16:
                    print("Sorry, not enough coffee beans!")
                elif self.cups < 1:
                    print("Sorry, not enough disposable cups!")
                else:
                    print("Something has gone wrong!!")

        elif coffee_type == "2":
            if self.water >= 350 and self.milk >= 75 and self.beans >= 20 and self.cups >= 1:
                self.money += 7
                self.water -= 350
                self.milk -= 75
                self.beans -= 20
                self.cups -= 1
                print("I have enough resources, making you a coffee!")
            else:
                if self.water < 350:
                    print("Sorry, not enough water!")
                elif self.milk < 75:
                    print("Sorry, not enough milk!")
                elif self.beans < 20:
                    print("Sorry, not enough coffee beans!")
                elif self.cups < 1:
                    print("Sorry, not enough disposable cups!")
                else:
                    print("Something has gone wrong!!")

        elif coffee_type == "3":
            if self.water >= 200 and self.milk >= 100 and self.beans >= 12 and self.cups >= 1:
                self.money += 6
                self.water -= 200
                self.milk -= 100
                self.beans -= 12
                self.cups -= 1
                print("I have enough resources, making you a coffee!")
            else:
                if self.water < 200:
                    print("Sorry, not enough water!")
                elif self.milk < 100:
                    print("Sorry, not enough milk!")
                elif self.beans < 12:
                    print("Sorry, not enough coffee beans!")
                elif self.cups < 1:
                    print("Sorry, not enough disposable cups!")
                else:
                    print("Something has gone wrong!!")
        else:
            print("Coffee type invalid, please try again.")

    def fill(self):
        water_add = int(input("How much water do you want to want to add: "))
        milk_add = int(input("How much milk do you want to add: "))
        beans_add = int(input("How much coffee beans do you want to add: "))
        disposable_cups_add = int(input("How many cups do you want to add: "))
        self.water += water_add
        self.milk += milk_add
        self.beans += beans_add
        self.cups += disposable_cups_add

    def take(self):
        print("I gave you $" + str(self.money))
        self.money -= self.money


cm = CoffeeMachine(400, 540, 120, 9, 550)

# Waiting for user input loop
action = input("Write action (buy, fill, take, remaining, exit): ")
while action != "exit":
    if action == "remaining":
        cm.remaining()
        action = input("Write action (buy, fill, take, remaining, exit): ")

    elif action == "buy":
        coffee_type = input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu: ")
        if coffee_type == "back":
            action = input("Write action (buy, fill, take, remaining, exit): ")
        else:
            cm.buy(coffee_type)
            action = input("Write action (buy, fill, take, remaining, exit): ")

    elif action == "fill":
        cm.fill()
        action = input("Write action (buy, fill, take, remaining, exit): ")

    elif action == "take":
        cm.take()
        action = input("Write action (buy, fill, take, remaining, exit): ")
