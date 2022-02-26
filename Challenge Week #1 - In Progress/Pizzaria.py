print("      Welcome to T.W.C Pizzaria - Here Is The Most Updated Menu             ")
print(" __________________________________________________________________________ ")
print("|  644 Topsail Rd,                                Hours - 10AM - 2AM       |")
print("|     A1E 2E3              T.W.C Pizzeria         Phone - (709)-420-4200   |")
print("|________________________________________________________________________  |")
print("|   PIZZA SPECIALS                                  PIZZA TOPPINGS         |")
print("|   ______________                                  ______________         |")
print("|   1. Meat Lovers          2. Veggie             * Pepperoni              |")
print("|   Small:  $15.99         Small:  $13.99         * Mushrooms              |")
print("|   Medium: $18.99         Medium: $16.99         * Green Peppers          |")
print("|   Large:  $20.99         Large:  $18.99         * Chicken($1.00)         |")
print("|                                                 * Meatballs              |")
print("|   3. Supreme              4. Hawaian            * Onions                 |")
print("|   Small:  $15.99         Small:  $15.99         * Ham                    |")
print("|   Medium: $18.99         Medium: $16.99         * Goat Cheese            |")
print("|   Large:  $18.99         Large:  $16.99         * Pineapple              |")
print("|                                                 * Anchovies              |")
print("|   PASTA                                                                  |")
print("|   _____                                                                  |")
print("|   4. Spaghetti ---------------------------------  $15.99                 |")
print("|   5. Fettuccine Alfredo ------------------------  $20.99                 |")
print("|   4. Veggie House Spaghetti --------------------  $17.99                 |")
print("|__________________________________________________________________________|")
print("|   DRINKS                      PRICE             KIDS CORNER              |")
print("|   _____                       _____             ___________              |")
print("|   5. Diet Pepsi   355mL       $2.99         12. Mini Pizzas(2)   $7.99   |")
print("|   6. Mtn Dew      355mL       $2.99         13. Chicken Fingers  $8.99   |")
print("|   7. Fruitopia    355mL       $2.99         14. Spaghetti        $10.99  |")
print("|   8. Root Beer    355mL       $2.99                                      |")
print("|   9. Diet Pepsi      2L       $4.49                                      |")
print("|   10. Mountain Dew   2L       $4.99                                      |")
print("|   11. Root Beer      2L       $4.99                                      |")
print("|                                                      T.W.C Pizzeria      |")
print("|                                                      --------------      |")
print("|__________________________________________________________________________|")

while True:
    Name = input("Welcome to T.W.C Pizzeria!! - Please Enter Your First Name: ").capitalize()
    if Name == "":
        print("Error - Name Cannot Be Blank - Please Re-Enter.")
    elif Name == "123456789":
        print("Error - First Name Cannot Contain Numbers - Please Re-Enter.")
    else:
        break

while True:
    Name = input("Please Enter Your Last Name: ").capitalize()
    if Name == "":
        print("Error - Last Name Cannot Be Blank - Please Re-Enter.")
    elif Name == "123456789":
        print("Error - Name Cannot Contain Numbers - Please Re-Enter.")
    else:
        break

while True:
    PhonNum = input("Please Enter Your Phone Number ")

while True:
        print()
        Choice = int(input("Please enter a number from the previous Menu::  "))
        print()
        if Choice == Choice: