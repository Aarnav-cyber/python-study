print("WELCOME TO MENU MAKER")

menu1 = []
menu2 = []


print("How many items would you like in your menu?")
num_items = int(input("Enter a number: "))

print("Enter values for menu1: ")
for i in range(num_items):
    value = input(f"Enter value {i+1}: ")
    menu1.append(value)

print("Enter values for menu2: ")
for i in range(num_items):
    value = input(f"Enter value {i+1}: ")
    menu2.append(value)

big_menu = menu1 + menu2

"""for x in menu1:
        print(" \n", x)

for y in menu2:
        print(" \n", y)"""

print("Final combined menu is: ")
print(big_menu)

input(str("Your choice: "))

