'''
Copyright © Jordan Lewis 2015 All Rights Reserved
This code is distributed under the Creative Commons Attribution ShareAlike 3.0 Licence

When I wrote this, only God and I understood what I was doing
Now, God only knows

WARNING:	The code that follows may make you cry;
            A Safety Pig has been provided below for your benefit
                         _
 _._ _..._ .-',     _.._(`))
'-. `     '  /-._.-'    ',/
   )         \            '.
  / _    _    |             \
 |  a    a    /              |
 \   .-.                     ;  
  '-('' ).-'       ,'       ;
     '-;           |      .'
        \           \    /
        | 7  .__  _.-\   \
        | |  |  ``/  /`  /
       /,_|  |   /,_/   /
          /,_/      '`-'
'''

# Import the necessary resources
import os
import time
from random import randint

# Global Variables to be accessed later
number = None
quiz_bool = None

# Function for clearing the screen
def cls():
    os.system(['clear','cls'][os.name == 'nt'])

# Function for asking the user for a number, it will keep asking until it gets valid input
def askForNumber():
    global number # Modify number to become a global variable
    
    # If the user enters anything other than a number, he/she will be re-prompted, this could pretty much go forever
    try:
        number = int(raw_input("Enter a number to have the times table displayed for you"))
    except:
        askForNumber() # Call this function if the input is not valid

# Function for asking whether or not the user wants to do the quiz, it will keep asking until it gets valid input
def askForQuiz():
    global quiz_bool # Modify quiz_bool to become a global variable
    
    # Ask the user
    quiz_str = raw_input("Would you like to be quizzed on this times table? Enter yes or no.")
    quiz_str = quiz_str.lower() # Convert the user input to an all lowercase string
    if (quiz_str == 'yes'):
        quiz_bool = True
    elif (quiz_str == 'no'):
        quiz_bool = False
    else:
        askForQuiz() # If it is neither yes or no, then call this function again to ask the user again

# The main function, which will be called when the program runs from the console    
def main():    
	
    cls() # Clear the screen incase there is anything above this program on the console for UI/UX
	
	# Ask for the number to be used as the base in the time table
    askForNumber()
    
    print "Times table for %i from 1 to 12"
    for i in range (1,13): # Print out the time table (13 Exclusive)
        print '%i x %i = %i' % (number, i, (number*i))
    
    #time.sleep(3) # Give the user some time to have a look at the times table
    
    for i in (1,3): # Give the user some time to have a look at the times table
        print "."	# Dots are for UI/UX
    	time.sleep(1)
    
    askForQuiz() # Ask the user if he/she wants to be quizzed
    
    # If the user wants to be quizzed
    if (quiz_bool):
        print "Quiz will begin in..."
        
        # Countdown from 5 seconds before the quiz starts, just a UI/UX thing I wanted to add
        for i in range (0,5):
            print str(5-i)
            time.sleep(1)
        
        cls() # Clear the screen
        
        values_to_quiz = [] # Declare variable, which is an array which will contain the values used to quiz the user.
        while len(values_to_quiz) < 5: # While there is less than 5 values to quiz the user with, do...
            random_int = randint(1,12) # Generate a random integer between 1 and 12 inclusive
            if (random_int in set(values_to_quiz)): # If the randomly generated number exists in the array, do nothing
                pass
            else: # If the randomly generated number does not exist in the array add it to the end of the array
                values_to_quiz.append(random_int)
        
        answers_correct = 0 # Variable to store the number of correct answers
        for to_quiz in values_to_quiz: # For every value in the array with randomly generated numbers between 1 to 12 inclusive
            try: # Try incase the user enters something stupid
                answer = int(raw_input("What is %i x %i?" % (number, to_quiz))) # Get the user to enter an answer and convert it to an integer, if the user enters something stupid, the program will jump to the except instead of crashing because of the conversion error
                if (answer == number*to_quiz): # Check if the answer the user entered is correct
                    answers_correct += 1 # If the answer is correct, award a mark
            except: # If the user enters something stupid such as a non-number, he/she will not be awarded a mark
                pass
                
            cls() # Clear the screen after each question, for UI/UX
            
        # Give the user his/her score out of five after the quiz is complete    
        print "You got %i/5 in the quiz." % answers_correct
        
        time.sleep(3) # Wait a few seconds for the user to see his/her score
    cls() # Clear the screen to end the program
                
# This is the boiler plate stuff that should be in the marking criteria
if __name__ == '__main__':
    main()