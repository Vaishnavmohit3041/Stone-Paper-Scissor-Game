
# Importing Module for Compuer Selecrion
import random

# Choices for Computer
choice=['Stone','Paper','Scissor']

# Choices for Feedback
feedback_choice=['P','B','A','G','E']

# Score of Computer and User
computer_score=0
user_score=0

#Loop for Continue the match
while True:

    # Asking to User what is his choice
    User=input("\n'S' for Stone\n'P' for Paper\n'C' for Scissor\n'Q' for Quit\n" )
    
    # Computer Choice selection from choice list
    Computer=random.choice(choice)

    # If User choose Stone then which function is to be performed
    if User=='S':
         print("\nYour Choice is Stone")
         print('Computer Choice is',Computer,'\n')
         if Computer=='Stone':
             computer_score+=1
             user_score+=1
             print('Its Tie so 1 Point goes to each\nComputer Score is',computer_score,'\nYour Score is',user_score)
         elif Computer=='Scissor':
             user_score+=1
             print('Stone break the Scìssor so 1 Point goes to You\nComputer Score is',computer_score,'\nYour Score is',user_score)
         else:
            computer_score+=1
            print('Paper cover the Stone so 1 Point goes to Computer\nComputer Score is',computer_score,'\nYour Score is',user_score)        
            
    # If User choose Paper then which function is to be performed
    elif User=='P':
        print("\nYour Choice is Paper")
        print('Computer Choice is ',Computer,'\n')
        if Computer=='Paper':
            computer_score+=1
            user_score+=1
            print('Its Tie so 1 Point goes to each\nComputer Score is',computer_score,'\nYour Score is',user_score)
        elif Computer=='Stone':
            user_score+=1
            print('Paper cover the Stone so 1 Point goes to You\nComputer Score is',computer_score,'\nYour Score is',user_score)
        else:
            computer_score+=1
            print("Scissor cuts the Paper so 1 Point goes to Computer\nComputer Score is",computer_score,'Your Score is',user_score)
            
        
     # If User choose Scissor then which function is to be performed   
    elif User=='C':
        print('\nYour Choice is Scissor')
        print('Computer Choice is ',Computer,'\n')
        if Computer=='Scissor':            
            user_score+=1
            computer_score+=1
            print('Its Tie so 1 Point goes to each\nComputer Score is',computer_score,'Your Score is',user_score)
        elif Computer=='Paper':          
            user_score+=1
            print('Scissor cuts the Paper so 1 Point goes to You\nComputer Score is',computer_score,'Your Score is',user_score)
        else:            
            computer_score+=1
            print('Stone break the Scissor so 1 Point goes to Computer\nComputer Score is',computer_score,'\nYour Score is',user_score)
        
     # If user want to be Quit   
    elif User=='Q':
        print('\nComputer score is',computer_score,'Your Score is',user_score)
        if computer_score==user_score:
            print('\nMatch is Tie')
        elif computer_score>=user_score:
            print('\nOh!, You Lost the Match.')
        else:
            print('\nCongratulations! You Won the Match')
            
         # for feedback of user
        while True:
            feedback=input("\nHow much you like this game?\n'E' for Excellent\n'G' for Good\n'A' for Average\n'B' for Bad\n'P' for Poor\n")
            if feedback in feedback_choice:
                print('\nThanks for your feedback')
                break
            else:
                print('\nPlease rewrite again in a proper way.')
                
        break
        
# If user make mistake in type         
    else:
        print("\nYour Choice is out of the section please rewrite again from only this.")


