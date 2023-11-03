import random

def yes_no_checker(question, valid_list, error):

    valid = False
    while not valid:

        response = input(question).lower() # Ask user for input

        for item in valid_list:

            if response == item[0] or response == item: 
                return item[0]

        print(error) # Show error if item not in list
        continue

def num_check(question, low, high):

    error = "Please enter a whole number between {} and {} \n".format(low, high)

    valid = False
    while not valid:

        response = (input(question))

        if response == "xxx":       # check if response is xxx
            return "x"
    
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

    # Welcome user when program is first run.

    print("\n\nWelcome!!!")

    # Ask user if they want to see the instructions
    see_instructions = yes_no_checker ("\nWould you like to see the instructions? ", yes_no_list, yes_no_error)

    if see_instructions == "x":
        break

    elif see_instructions == "y":
        print("\nThese are the instructions!!\nYou can do this quiz with any amount of questions between 1 and 169\nYou can enter 'xxx' at any time to quit.")


    # Quiz setup. Loop to skip welcome section if quiz is played again
    play_again= "y"
    while play_again == "y":

        # Define variables here to reset for new round
        asked_before = []
        user_answers = []
        question_amount = 0
        correct = 0

        # ask user for game type
        question_amount = num_check("\nHow many questions would you like to answer? ", 1 , 169)

        if question_amount == "x":          # Break
            break

        else:
            print("\nThis is a {} question quiz!".format(question_amount))

        question_number = 0
        # Quiz loop
        while question_number < question_amount:

            # attempt to find a question that has not been asked
            question_attempt = True
            while question_attempt == True:

                first_number = random.randint(0,12)                  
                second_number = random.randint(0,12)
                correct_answer = first_number * second_number
                question = ("{} x {} = ".format(first_number, second_number)) 


                if question in asked_before:    # Generate another question if the previous question has already been asked
                    break

                else:                           # Ask the question to the user if not in asked before list
                    
                    print("Question {}:".format(question_number+1))
                    user_input = num_check(question, 0 , 999)
                    print()
                    asked_before.append (question)          # Add question to asked before

                    if user_input == "x":
                        break
                
                    elif int(user_input) == correct_answer:
                        feedback = ("You answered correctly")
                        correct = correct +1

                    else:
                        feedback = ("The correct answer was {}".format(correct_answer))


                    # Generate feedback and add to list
                    outcome = ("Question {}: {} x {} = {}. {} ".format(question_number +1, first_number, second_number, user_input, feedback))  
                    user_answers.append (outcome)
                    question_number = question_number +1
                    break

            if user_input == "x":
                break

        # End of quiz summary
        print("********** Your answers **********")
        for question in user_answers:
            print (question)

        percent_correct = correct / question_amount
        print("\nYou got {}% correct".format(percent_correct * 100 ))
        print ("This means you answered {} out of {} questions correctly.".format(correct, question_amount))

                    
        play_again = yes_no_checker("Would you like to play again? Y / N ", yes_no_list , yes_no_error)   

    break

print("Thanks for playing!!!")
