# HW1 Q15
# Name: William Eng
# Description: Takes a number between 0-100 and prints the corresponding letter grade to the screen

# •	(1 point) Ask the user to enter an integer between 0-100
print("Enter an integer between 0-100:")
# •	(1 point) Save the user input to a variable
userNumber = int(input())
# •	Use a series of if, elif, and else statements to print the correct letter grade and GPA to the screen based on this list: (11 points)
# o	95 or above 		4.0, A
# o	90-94			3.7, A-
# o	85-89			3.3, B+
# o	80-84			3.0, B
# o	75-79			2.7, B-
# o	70-74			2.3, C+
# o	65-69			2.0, C
# o	60-64			1.7, C-
# o	55-59			1.3, D+
# o	50-54			1.0, D
# o	0-49			0.0, F
# •	Use a loop to allow the user to enter more than one number. The loop stops if the user enters a -1. (2 points)
# •	(5 points) Check if the user enters an integer lower than -1 or greater than 100 and print an error message
# •	You must comment your code (5 points)
# initialize user choice
userChoice = 0
while(userChoice != '-1'):
    if (userNumber >= 95 and userNumber <=100):
        print("Your GPA and grade are: 4.0, A")
    elif(userNumber >= 90 and userNumber <= 94):
        print("Your GPA and grade are: 3.7, A-")
    elif(userNumber >= 85 and userNumber <= 89):
        print("Your GPA and grade are: 3.3, B+")
    elif(userNumber >= 80 and userNumber <= 84):
        print("Your GPA and grade are: 3.0, B")
    elif(userNumber >= 75 and userNumber <= 79):
        print("Your GPA and grade are: 2.7, B-")
    elif(userNumber >= 70 and userNumber <= 74):
        print("Your GPA and grade are: 2.3, C+")
    elif(userNumber >= 65 and userNumber <= 69):
        print("Your GPA and grade are: 2.0, C")
    elif(userNumber >= 60 and userNumber <= 64):
        print("Your GPA and grade are: 1.7, C-")
    elif(userNumber >= 55 and userNumber <= 59):
        print("Your GPA and grade are: 1.3, D+")
    elif(userNumber >= 50 and userNumber <= 54):
        print("Your GPA and grade are: 1.0, D")
    elif(userNumber >= 0 and userNumber <= 49):
        print("Your GPA and grade are: 0.0, F")
    else:
        print("ERROR: You have inputted an integer lower than -1 or greater than 100")
    print("Would you like to enter another integer between 0-100?  Please enter any integer other than -1.  If you would like to exit, please enter -1")
    userChoice = input()
    # allow user choice to be string to allow them to enter nothing
    if(userChoice != '-1'):
        print("Enter an integer between 0-100:")
        userNumber = int(input())