print("Get ready to play rock paper scissors")
#to print rock image
def rockimg():
    print('''
       _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
    ''')
#to print paper image
def paperimg():
    print('''
         _______
    ---'    ____)____
               ______)
              _______)
             _______)
    ---.__________)
    ''')
#to print scissors image
def scissorsimg():
    print('''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
    ''')
#to define rock, paper and scissors as specific values
rock=1
paper=2
scissors=3
#to initialise scores as 0
computer_score=0
user_score=0
while True:
 choice = input("Would you like to play? y/n:")
 if choice == "y":
    user_choice=int(input('''Rock is 1, paper is 2 and scissors is 3
    which one do you pick?:'''))
    #to print rock, paper or scissors for user choice
    if user_choice==1:
     print("you picked rock")
     rockimg()
    elif user_choice==2:
     print("you picked paper")
     paperimg()
    elif user_choice==3:
     print("you picked scissors")
     scissorsimg()
    else:
     print("That is an invalid option")
    import random
   # to give rock paper or scissors for computer choice
    RandomNumber= random.randint(1,3)
   #to define the rules of the game
    if RandomNumber == 1:
     print("computer picked rock")
     rockimg()
     if RandomNumber and user_choice==1:
      user_score+=0
      computer_score+=0
      print("No point")
     elif RandomNumber==1 and user_choice==2:
      user_score+=1
      computer_score+=0
      print(" You got a point")
     elif RandomNumber==1 and user_choice==3:
      user_score+=0
      computer_score+=1
      print("You got no point and the computer got a point")
    elif RandomNumber==2:
     print("computer picked paper")
     paperimg()
     if RandomNumber and user_choice == 2:
      user_score+=0
      computer_score+= 0
      print("No point")
     elif RandomNumber == 2 and user_choice == 1:
      user_score+=0
      computer_score+=1
      print("You got no point and the computer got a point")
     elif RandomNumber == 2 and user_choice == 3:
      user_score+=1
      computer_score+=0
      print("You got a point")
    elif RandomNumber==3:
     print("computer picked scissors")
     scissorsimg()
     if RandomNumber and user_choice == 3:
      user_score+=0
      computer_score+=0
      print("No point")
     elif RandomNumber == 3 and user_choice == 1:
      user_score+=1
      computer_score+=0
      print(" You got a point")
     elif RandomNumber == 3 and user_choice == 2:
      user_score+=0
      computer_score+=1
      print("You got no point and the computer got a point")
 #to stop playing, this will end the game
 elif choice=="n":
     #to calculate final score
     user_score+=0
     computer_score+=0
    #to display final score
     print("Your final score is " +str(user_score))
     print("The computer's final score is "+str(computer_score))
    #to display winner
     if user_score>computer_score:
         print("You won")
     elif computer_score>user_score:
         print("Computer won")
     else:
         print("It's a tie")
     break
