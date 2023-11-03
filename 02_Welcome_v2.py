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
    response = (input(question))
    if response == "xxx":
        return response
    
    valid = False
    while not valid:
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

yes_no_list = ["yes", "no", "xxx"]
yes_no_error = "Please enter 'yes', 'no' or 'xxx' to continue"

# program start
program = "running"
while program == "running":

    print("Welcome!!!")

    # ask user if they want to see the instructions
    print("This is how the quiz works!")
    see_instructions = yes_no_checker ("\nWould you like to see the instructions? ", yes_no_list, yes_no_error)
    if see_instructions == "xxx":
        break
    elif see_instructions == "y":
        print("\nThese are the instructions")

    else:
        print("do not show instructions")

    play_again = "y"
    while play_again == "y":

        print("*Game plays*")
        play_again = yes_no_checker("Do you want to play again? ", yes_no_list, yes_no_error)

    print("thanks for playing !!!")