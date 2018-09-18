from random import *
from calc import calculate




def generate_quiz():
    # Hint: Return [x, y, op, result]
    
    dif = randint(-1, 1)
    x = randint(0,9)
    y = randint(0,9)
    op = choice(["+","-","*","/"])
    result = calculate(x, y, op) + dif
    return [x, y, op, result]
    
# ez = generate_quiz()
# print(ez)


def check_answer(x, y, op, result, user_choice):

    if calculate(x, y, op) == result:
        if user_choice == True:
            return True
        elif user_choice == False:
            return False

    elif calculate(x, y, op) != result:
        if user_choice == True:
            return False
        elif user_choice == False:
            return True

    
 

    
