import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
user_input = int(input("What do you choose? 0 for Rock , 1 for Paper , 2 for Scissor "))
computer_choice = random.randint(0,2)
print(f"Computer Choose {computer_choice}")
if user_input < 0 and user_input >2:
    print("Invalid Input")
elif user_input == computer_choice :
    print("It's Draw")
elif user_input == 0 and computer_choice == 1:
    print("You lose")
elif user_input == 0 and computer_choice == 2 :
    print("You win")
elif user_input == 1 and computer_choice == 0 : 
    print("You win")
elif user_input == 1 and computer_choice == 2 :
    print("You lose")
elif user_input == 2 and computer_choice == 1 : 
    print("You win")
elif user_input == 2 and computer_choice == 0 :
    print("You lose")