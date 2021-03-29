import random

# Define the function 
def guess(x):
    random_number = random.randint(1,x)

    num = 0
    # Loop untill guess is equal to random number
    while(num != random_number):
        num = int(input("Please enter a number between 1 and 10 : "))

        # 3 possibilities 
        if random_number < num:
            print(f"Oh god! Too high... {num}")

        elif num < random_number:
            print(f"Oh god! Too low... {num}")

    print(f"Perfect! The number is {num}")

guess(10)




