import random

'''
for Rock 1
for Paper -1
for Scisors 0

'''
sys = random.choice([1,-1,0])
lst = ["r","s","p"]
a = None
while a is None :
    y_choice = (input("Enter you choice  { r,p,s} :")).lower()
    if (y_choice not in lst):
        print("Invalid Choice! enter only {r,p,s}")
        a = None
    else :
        a = 1
    

youdict = { "r": 1 , "p": -1 , "s": 0}

you = youdict[y_choice]
Rev_Dict = { 1: "Rock" ,-1 : "Paper " , 0 : "Scissors"}

print(f"You chose {Rev_Dict[you]} \nSystem chose {Rev_Dict[sys]} ")

if sys == you :
    print("It's A DRAW !...")
else :
    if (sys == 1 and you == -1)  or \
       (sys == -1 and you == 0 )or \
       (sys == 0 and you == 1) :
        print("YOU WON !...")
    else :
        print("YOU LOST !...")


# import random

# def get_user_choice():
#     valid_choices = ['rock', 'paper', 'scissors']
#     user = input("Enter rock, paper, or scissors: ").lower()
#     if user not in valid_choices:
#         print("Invalid input. Please choose rock, paper, or scissors.")
#         return None
#     return user

# def determine_winner(user, comp):
#     if user == comp:
#         return "It's a tie!"
#     if (user == "rock" and comp == "scissors") or \
#        (user == "paper" and comp == "rock") or \
#        (user == "scissors" and comp == "paper"):
#         return "You win!"
#     return "Computer wins!"

# def play():
#     user_choice = None
#     while user_choice is None:  # Keep asking until user gives valid input
#         user_choice = get_user_choice()

#     comp_choice = random.choice(["rock", "paper", "scissors"])
#     print(f"Computer chose: {comp_choice}")
#     result = determine_winner(user_choice, comp_choice)
#     print(result)

# play()


        

