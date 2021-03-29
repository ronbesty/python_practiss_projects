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

# guess(10)

# Write a function to make computer guess your number 
def comp_guess(x):
    low = 1
    high = x 

    feedback = ""
    # loop to check if the number is right
    while feedback != "c":
        if low != high:
            random_num = random.randint(low,high)
        else:
            random_num = low #To prevent the state of Low == high

        # take the feedback from the user 
        feedback = input(f"Whats on your mind man? is it {random_num}? ")

        # There are two possibilities 
        if feedback == "h":
            high = random_num - 1
        
        elif feedback == "l":
            low = random_num + 1
    print("Bang on!")

comp_guess(10)





