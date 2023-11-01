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

    print("Welcome!!!")

    # ask user if they want to see the instructions
    print("This is how the quiz works!")
    see_instructions = input_checker ("\nWould you like to see the instructions? ", "Y/N", "enter yes or no")
    if see_instructions == "xxx":
        break
    elif see_instructions == "y":
        print("\nThese are the instructions")

    play_again= "y"
    while play_again == "y":

        # ask user for game type
        quiz_type = input_checker("Would you like to play 12x12? press y for yes or n for 10 questions ", "Y/N", "press y or n")

        if quiz_type == "xxx":
            break

        elif quiz_type == "y":
            print("game type 12 x 12")

        else:
            print("game type 10 questions")



        while quiz_type == "y":                 # loop for game type 12x12
            print("*Quiz type 12 x 12 plays*")
            break
 

        while quiz_type == "n":
            print("*quiz type 10 questions plays*")
            break

        play_again = input_checker("would you like to play again? ", "Y/N", "press y or n")

    print("thanks for playing!!!")
    break
