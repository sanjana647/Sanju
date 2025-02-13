import random
a=["Rock","Paper","Scissor"]
computer_choice=random.choice(a)

computer_score=0
player_score=0

while True:

    player_choice=input("Enter your choice:").capitalize()
    if player_choice==computer_choice:
        print("Tie")
        computer_score+=1
        player_score+=1
    elif player_choice=="Rock":
        if computer_choice=="Paper":
            print("Computer wins")
            computer_score+=1
        if computer_choice=="Scissor":
            print("Player wins")
            player_score+=1
    elif player_choice=="Paper":
        if computer_choice=="Rock":
            print("Player wins")
            computer_score+=1
        if computer_choice=="Scissor":
            print("Computer wins")
            computer_score+=1
    elif player_choice=="Scissor":
        if computer_choice=="Rock":
            print("Computer wins")
        if computer_choice=="Paper":
            player_score+=1
    else:
        print("Final scores")
        print(player_score)
        print(computer_score)
        break

        






