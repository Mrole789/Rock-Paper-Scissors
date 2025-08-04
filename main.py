import random
art = ["""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""",
"""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""",
"""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""]
print("Rock, Paper Scissors")
choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for scissors:\n"))

if choice >= 0 and choice <= 2:
    echoice = art[choice]
    print(f"You chose: {echoice}")
    
    options = [0,1,2]
    pcchoice = random.choice(options)

    epcchoice = art[pcchoice]
    print(f"The computer chose: {epcchoice}")


    if pcchoice == choice:
        print("Its a draw")
    elif pcchoice == 0 and choice == 1:
        print("You win")
    elif pcchoice == 0 and choice == 2:
        print("The computer wins")
    elif pcchoice == 1 and choice == 0:
        print("The computer wins")
    elif pcchoice == 1 and choice == 2:
        print("You win")
    elif pcchoice == 2 and choice == 0:
        print("You win")
    elif pcchoice == 2 and choice == 1:
        print("The computer wins")
else:
    print("You have type the wrong input. You lose.")
