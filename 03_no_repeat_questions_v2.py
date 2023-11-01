import random
asked_before = []
program = "running"
question_number = 0

while program == "running":


    while question_number <169 :

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
    break

