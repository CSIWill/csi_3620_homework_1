# HW1 Q16
# Name: William Eng
# Description: Playing with random values and lists

# 1.	(2 points) Generates a list of 10 numbers containing random values between 0-100, inclusive
# 2.	(1 point) Prints to the screen the list of numbers
# 3.	(1 point) Prints to the screen the smallest number in the list
# 4.	(1 point) Prints to the screen the largest number in the list
# 5.	(1 point) Prints to the screen the average of the numbers in the list
# 6.	(1 point) Prints to the screen the sorted list, from lowest to highest value
# 7.	(1 point) Prints to the screen the median of the numbers in the list
# 8.	(1 point) Includes comments

import random
# initialize empty list
randList = []
# for loop to append 10 values to empty list
for i in range (10):
    # value between 0 - 100 inclusive and append to empty list
    randList.append(random.randint(0,100))
# print to screen
print(f"Randomly generated list: {randList}")
# print smallest number
print(f"The smallest number is: {min(randList)}")
# print the largest number
print(f"The largest number is: {max(randList)}")
# print average of numbers
# no average command but I do know sum command and how many elements
print(f"The average is: {sum(randList)/10}")
# print sort list, doesn't matter if the original list is altered to the sorted view
randList.sort()
print(f"The sorted list: {randList}")
# print median, since it is 10 elements, we need the average of the 5th and 6th elements
print(f"The median of the list is: {(randList[5]+randList[6])/2}")
