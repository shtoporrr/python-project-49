import random

DESCRIPTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def play_rounds():
    rounds = 3
    
    for _ in range(rounds):
        number = random.randint(1, 100)
        print(f"Question: {number}")
        
        user_answer = input("Your answer: ").strip().lower()
        correct_answer = "yes" if is_prime(number) else "no"
        
        if user_answer == correct_answer:
            print("Correct!")
        else:
            print(f"'{user_answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.")
            return False
    return True
