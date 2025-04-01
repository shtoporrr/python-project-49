import random


DESCRIPTION = "What number is missing in the progression?"


def generate_progression():
    length = random.randint(5, 10)
    start = random.randint(1, 50)
    step = random.randint(1, 10)
    progression = [start + i * step for i in range(length)]
    hidden_index = random.randint(0, length - 1)
    correct_answer = progression[hidden_index]
    progression[hidden_index] = ".."
    return progression, correct_answer


def play_rounds():
    rounds = 3
    
    for _ in range(rounds):
        progression, correct_answer = generate_progression()
        progression_str = " ".join(map(str, progression))
        print(f"Question: {progression_str}")
        
        user_answer = input("Your answer: ").strip()
        try:
            if int(user_answer) == correct_answer:
                print("Correct!")
            else:
                print(f"'{user_answer}' is wrong answer ;(. 
                Correct answer was '{correct_answer}'.")
                return False
        except ValueError:
            print(f"'{user_answer}' is not a valid number. 
            Correct answer was '{correct_answer}'.")
            return False
    return True
