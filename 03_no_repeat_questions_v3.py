import random
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




print()
question_amount = num_check("\nHow many questions would you like to answer? ", 1 , 169)

if question_amount == "xxx":          # Break
    print()

else:
    print("\nThis is a {} question quiz!".format(question_amount))

question_number = 0
asked_before = []
program = "running"
question_number = 0

while program == "running":


    while question_number <question_amount :

        question_attempt = True
        while question_attempt == True:

            first_number = random.randint(0,12)                  
            second_number = random.randint(0,12)
            question = ("{} x {}".format(first_number, second_number)) 

            if question in asked_before:
                print("{} asked before".format(question))
                
                break

            else:
                print("{} not asked before".format(question))
                asked_before.append (question)
                question_number = question_number +1
                break
                
                
    print(asked_before)
    print("{} is the length of asked before list.".format(len(asked_before)))
    break
