from quiz_database import question_bank
from quiz_database import options

print("_______________________________________________________") 
print("welcome to Quize game!!!")


score=0
def check_answer(user_guess,currect_answer):
    if user_guess==currect_answer:
        return True
    else:
        return False
    

for question_num in range(len(question_bank)):
    print("____________________________________________")
    print(question_bank[question_num]["text"])
    for i in options[question_num]:
        print(i)
    guess=input("enter your number(a/b/c/d): ").lower()
    is_currect=check_answer(guess,question_bank[question_num]["answer"])
    if is_currect:
        print("Correct Answer!")
        score += 1
    else:
        print("Incorrect Answer!")
        print(f"the currect answer is {question_bank[question_num]['answer']}")
    
    print(f"your current score is {score}/{question_num+1} ")

print(f"your have given {score} currect answers")
print(f"your score is {(score/len(question_bank))+100} %")

