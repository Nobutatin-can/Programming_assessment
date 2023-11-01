import random

play_again = ("")
while play_again == "":
    print ("Timetables quiz ")
    print("Press <enter> anytime to quit")

    summary = []
    correct = 0
    question_counter = 0

    while question_counter < 10 :

        print ("Question {}".format (question_counter +1))      # Tell user what question they are on

        first_number = random.randint(0,12)                     # Generate first and second number and find the answer
        second_number = random.randint(0,12)
        correct_answer = first_number * second_number

        user_input = input ("{} x {} = ".format(first_number, second_number))  
        print()

        if int(user_input) == correct_answer:
            feedback = ("You answered correctly")
            correct = correct +1

        else:
            feedback = ("The correct answer was {}".format(correct_answer))

        outcome = ("Question {}: {} x {} = {}. {} ".format(question_counter +1, first_number, second_number, user_input, feedback))  
        summary.append (outcome)

        question_counter = question_counter +1
        
    # Quiz summary

    print("********** Your answers **********")

    for question in summary:
        print (question)

    print("\nYou got {}% correct".format( correct * 10 ))
    print ("This means you answered {} out of 10 questions correctly.".format(correct))
    play_again = input("Press <enter> to play again or any key to quit. ")

print("Thanks for playing!!!")