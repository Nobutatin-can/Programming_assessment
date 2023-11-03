# yes no checker

def yes_no_checker(question, valid_list, error):

    valid = False
    while not valid:

        response = input(question).lower() # Ask user for input

        for item in valid_list:

            if response == item[0] or response == item: 
                return item[0]

        print(error) # Show error if item not in list
        print()
        continue

def num_check(question, low, high):
    error = "Please enter a whole number between {} and {} \n".format(low, high)

    
    valid = False
    while not valid:

        response = (input(question))
        if response == "xxx":
            return response
        try:
            # see if question is an int
            response = int(response)

            # Show user the ammount input
            if low <= response <= high:
                return response

            # output error when response is invalid
            else:
                print(error)
                continue

        except ValueError:
            print(error)
            continue

# Yes no checker
yes_no_list = ["yes", "no", "xxx"]

user_choice = " "

while user_choice != "x":

    user_choice = yes_no_checker("Choose yes or no): " , yes_no_list, "Please choose yes or no (or xxx to quit") #  Ask user for input then check if valid


    print("You chose {}".format(user_choice)) # Print the choice




# number checker
user_choice2 = " "
while user_choice2!= "x":

    answer = num_check("Please enter a number", 1, 10)

    # Tell the user their number
    print("Your number is {}".format(answer))