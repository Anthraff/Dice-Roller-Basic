

import random

roll_the_dice = True
while roll_the_dice == True:
    x = int(input("Which dice would you like to roll?(6,12,20): "))
    while x != 6 and x != 12 and x != 20:
        print("Please choose 6, 12, or 20")
        x = int(input("Which dice would you like to roll?(6,12,20): "))
    if x == 6:
        x = random.randint(1,6)
        print(x)
    elif x == 12:
        x = random.randint(1,12)
        print(x)
    else:
        x = random.randint(1,20)
        print(x)
    y = input("Would you like to roll again?(y or n): ")
    while y.lower() != "y" and y.lower() != "n":
        print("Please choose y or n")
        y = input("Would you like to roll again?(y or n): ")
    if y.lower() == "y":
        roll_the_dice = True
    else:
        roll_the_dice = False
            
