# HW1 Q14
# Name: William Eng
# Description: String Manipulation

# 1.	(1 point) Greets the user
print("Hello User")
# 2.	(1 point) Asks the user to enter a name
print("What is your name?")
# 3.	(1 point) Saves the input name as a variable
userName = input()
# 4.	(1 point) Removes whitespace to the left and right of the name, and saves it to a variable
stripName = userName.strip()
# 5.	(1 point) Prints the stripped name with first letters capitalized (title case)
print(f"Capital case: {stripName.title()}")
# 6.	(1 point) Prints the stripped name with all letters capitalized
print(f"Upper case: {stripName.upper()}")
# 7.	(1 point) Prints the stripped name with all letters uncapitalized
print(f"Lower case: {stripName.lower()}")
# 8.	(1 point) Prints the name as the user entered it
print(f"You entered: {userName}")
# 9.	(2 points) Make sure that your code is commented or you will lose points.
