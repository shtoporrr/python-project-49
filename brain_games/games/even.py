import random


DESCRIPTION = 'Answer "yes" if the number is even, otherwise answer "no".'


def play_rounds():
    rounds = 3
    
    for _ in range(rounds):
        number = random.randint(1, 100)
        print(f"Question: {number}")
        
        user_answer = input("Your answer: ").strip().lower()
        correct_answer = "yes" if number % 2 == 0 else "no"
        
        if user_answer == correct_answer:
            print("Correct!")
        else:
            print(f"'{user_answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.")
            return False
    return True
