import random

def input_checker(question, input_type, error):

    valid = False
    while not valid:

        response = input(question).lower()

        if response == "xxx":                       # Break if response is xxx
            return response
        

        elif input_type == "Y/N":                   # If input type Y / N, check if response valid

            if response == "yes":
                response = "y"
                return response

            elif response == "no":
                response = "n"
                return response

            elif response == "y" or response == "n":
                return response
            
            else:
                print(error)
                continue

        elif input_type == "answer":                # If input type is answer, check if response is valid

            try:
                response = int(response)
                return response

            except ValueError:
                print (error)
                continue
                
            
        else:
            print("!!!!! WARNING !!!!! THIS IS NOT A VALID INPUT TYPE !!!!!") # Tell programer that they have an invalid input type

            return response

    return response

# program start
program = "running"
while program == "running":

    # Welcome user when program is first run.

    print("Welcome!!!")

    # Ask user if they want to see the instructions
    see_instructions = input_checker ("\nWould you like to see the instructions? ", "Y/N", "Please enter 'yes' or 'no'. ")

    if see_instructions == "xxx":
        break

    elif see_instructions == "y":
        print("\nThese are the instructions!!\nYou can do this quiz with 10 or 169 questions\nYou can enter 'xxx' at any time to quit.")


    # Quiz setup. Loop to skip welcome section if quiz is played again
    play_again= "y"
    while play_again == "y":

        asked_before = []
        user_answers = []
        question_ammount = 0
        correct = 0

        # ask user for game type
        quiz_type = input_checker("\nWould you like to play 12x12? press Y for yes or N for 10 questions ", "Y/N", "Press y or n")

        if quiz_type == "xxx":          # Break
            break

        elif quiz_type == "y":
            question_ammount = 169      # For 12x12 grid
            print("169 question quiz")
            
        else:
            question_ammount = 10       # for 10 questions
            print("10 question quiz")


        # Quiz loop
        question_number = 0
        while question_number < question_ammount:

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
                    
                    user_input = input_checker(question, "answer", "Please enter a full number.")

                    asked_before.append (question)          # Add question to asked before

                    if user_input == "xxx":
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

            if user_input == "xxx":
                break


        if question_number == question_ammount:                      # Show stats if round is completed. Skip if not
            print("********** Your answers **********")

            for question in user_answers:
                print (question)

            print("\nYou got {}% correct".format( correct * 10 ))
            print ("This means you answered {} out of {} questions correctly.".format(correct, question_ammount))

                    
        play_again = input_checker("Would you like to play again? Y / N ", "Y/N", "Press Y or N to continue")   

    break

print("Thanks for playing!!!")
