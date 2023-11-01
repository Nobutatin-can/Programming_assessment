import random
questions = ["1 x 1", "1 x 2","1 x 3","1 x 4","1 x 5","1 x 6","1 x 7","1 x 8","1 x 9","1 x 10","1 x 11","1 x 12","2 x 1","2 x 2","1 x 1","1 x 1","1 x 1","1 x 1","1 x 1","1 x 1","1 x 1","1 x 1","1 x 1","1 x 1","1 x 1","1 x 1","1 x 1","1 x 1","1 x 1","1 x 1","1 x 1","1 x 1","1 x 1","1 x 1","1 x 1","1 x 1","1 x 1","1 x 1","1 x 1","1 x 1","1 x 1","1 x 1","1 x 1","1 x 1","1 x 1","1 x 1","1 x 1","1 x 1","1 x 1","1 x 1","1 x 1","1 x 1","1 x 1","1 x 1","1 x 1","1 x 1","1 x 1","1 x 1","1 x 1","1 x 1","1 x 1","1 x 1","1 x 1","1 x 1","1 x 1","1 x 1","1 x 1","1 x 1","1 x 1","1 x 1","1 x 1","1 x 1","1 x 1","1 x 1","1 x 1","1 x 1","1 x 1","1 x 1","1 x 1","1 x 1","1 x 1","1 x 1","1 x 1","1 x 1","1 x 1","1 x 1","1 x 1","1 x 1","1 x 1","1 x 1","1 x 1","1 x 1","1 x 1","1 x 1","1 x 1","1 x 1","1 x 1","1 x 1","1 x 1","1 x 1","1 x 1","1 x 1","1 x 1","1 x 1","1 x 1","1 x 1","1 x 1","1 x 1","1 x 1","1 x 1","1 x 1","1 x 1","1 x 1","1 x 1","1 x 1","1 x 1","1 x 1","1 x 1","1 x 1","1 x 1","1 x 1","1 x 1","1 x 1","1 x 1","1 x 1","1 x 1","1 x 1","1 x 1","1 x 1","1 x 1","1 x 1","1 x 1","1 x 1","1 x 1","1 x 1","1 x 1","1 x 1","1 x 1","1 x 1","1 x 1","1 x 1","1 x 1","1 x 1","1 x 1","1 x 1","1 x 1","1 x 1","1 x 1","1 x 1","1 x 1","1 x 1","1 x 1","1 x 1","1 x 1","1 x 1","1 x 1","1 x 1","1 x 1","1 x 1"]
program = "running"
question_number = 0

while program == "running":


    while question_number <169 :

        ask_question = True
        while ask_question == True:

            print (questions[0])
            del questions[0]
            print(questions)
            question_number = question_number +1
                
    print(questions)
    break
