import random


DESCRIPTION = "What is the result of the expression?"


def generate_round():
    operators = ['+', '-', '*']
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)
    op = random.choice(operators)
    question = f"{num1} {op} {num2}"
    
    if op == '+':
        correct_answer = num1 + num2
    elif op == '-':
        correct_answer = num1 - num2
    else:  # op == '*'
        correct_answer = num1 * num2

    return question, correct_answer
