from survey import  AnoymousSurvey
question = "What language did you first learn to speak?"
my_survey = AnoymousSurvey(question)

my_survey.show_question()

print("Enter 'q' at any time to quit")
while True:
    response = input("Language: ")
    if response == "q":
        break
    else:
        my_survey.store_response(response)

print("\nThank you to everyone who participated in this survey! ")
my_survey.show_result()
