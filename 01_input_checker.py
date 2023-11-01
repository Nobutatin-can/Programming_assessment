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


# Test loop
test_loop = "yes"
while test_loop == "yes":

    see_instructions = input_checker("\nWould you like to see the instructions ", "Y/N", "enter y or n")    # test for Y/N type
    if see_instructions == "xxx":
        print(see_instructions)
        break

    elif see_instructions == "y":
        print(see_instructions)
        print ("show instructions")

    else:
        print(see_instructions)
        print("Do not show instructions")


    answer_test = input_checker("\nWhat is your answer? ", "answer", "Enter your answer using numbers")     # test for answer type
    if answer_test == "xxx":
        print(answer_test)
        break
    else:
        print(answer_test)
        print("you answered")

    invalid_input_type = input_checker("\nThis is the test for invalid type ", "invalid type", "This is an error")  #test for invalid type
    if invalid_input_type == "xxx":
        print(invalid_input_type)
        break
    elif invalid_input_type == "option1":
        print(invalid_input_type)
        print("option 1")

    else:
        print(invalid_input_type)
        print("option 2")

    test_again = input_checker("\nTest again? ", "Y/N", "answer y or n ")
    if test_again == "y":
        print(test_again)
        continue
    else:
        print(test_again)
        break

print("Goodbye!!!")
        
