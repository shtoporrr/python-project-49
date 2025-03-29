import random

DESCRIPTION = "What is the result of the expression?"

def play_rounds():
    rounds = 3
    operators = ['+', '-', '*']
    
    for _ in range(rounds):
        num1 = random.randint(1, 100)
        num2 = random.randint(1, 100)
        op = random.choice(operators)
        expression = f"{num1} {op} {num2}"
        print(f"Question: {expression}")
        
        user_answer = input("Your answer: ").strip()
        
        if op == '+':
            correct_answer = num1 + num2
        elif op == '-':
            correct_answer = num1 - num2
        else:  # op == '*'
            correct_answer = num1 * num2
        
        try:
            if int(user_answer) == correct_answer:
                print("Correct!")
            else:
                print(f"'{user_answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.")
                return False
        except ValueError:
            print(f"'{user_answer}' is not a valid number. Correct answer was '{correct_answer}'.")
            return False
            
    return True
