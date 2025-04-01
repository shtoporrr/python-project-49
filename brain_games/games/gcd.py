import random
import math


DESCRIPTION = "Find the greatest common divisor of given numbers."


def play_rounds():
    rounds = 3
    
    for _ in range(rounds):
        num1 = random.randint(1, 100)
        num2 = random.randint(1, 100)
        print(f"Question: {num1} {num2}")
        
        user_answer = input("Your answer: ").strip()
        correct_answer = math.gcd(num1, num2)
        
        try:
            if int(user_answer) == correct_answer:
                print("Correct!")
            else:
                print(f"'{user_answer}' is wrong answer ;(. " +
                        f"Correct answer was '{correct_answer}'.")
                return False
        except ValueError:
            print(f"'{user_answer}' is not a valid number. " + 
                    f"Correct answer was '{correct_answer}'.")
            return False
            
    return True
