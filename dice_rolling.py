import random  
print("Dice Rolling Simulator")
while True:
    rolln=input("Roll the dice? (y/n):").lower()
    if rolln=="y":
        print("You rolled:",random.randint(1,6))
    else:
        print("Exit")
        break