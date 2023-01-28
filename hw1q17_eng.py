# HW1 Q17
# Name: Prof. Bowers
# Description: Function with an arbitrary number of arguments

# •	Call that function twice
# •	Use different arguments for each function call
# •	Use a different number of arguments for each function call
# •	Somehow access or modify each of the arguments inside your function
# •	Be commented

# Goal is to print back how many movies and list them alphabetically
def movieList(*movies):
    # create list from arbitrary number of inputs
    userList = [*movies]
    # print how many inputs were provided
    print(f"You have given {len(userList)} movies")
    # print the sorted list.  Do not need the original list
    userList.sort()
    # fix formatting of the list
    for movie in userList:
        print(movie.title())
        
# 4 movies not all formatted as titles properly
movieList('Star wars', 'stargate', 'star Trek', 'star quest')

# 6 movies not all formatted as titles properly
movieList('Top Gun', 'James Bond: dr. no', 'The Incredibles', 'The Fast and the furious: tokyo drift', 'blood Diamond')
