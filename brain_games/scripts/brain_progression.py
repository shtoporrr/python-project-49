import random


def generate_progression():
    length = random.randint(5, 10)
    start = random.randint(1, 50)
    step = random.randint(1, 10)
    
    progression = [start + i * step for i in range(length)]
    hidden_index = random.randint(0, length - 1)
    correct_answer = progression[hidden_index]
    progression[hidden_index] = ".."
    
    return progression, correct_answer


def progression_game():
    rounds = 3
    for _ in range(rounds):
        progression, correct_answer = generate_progression()
        progression_str = " ".join(map(str, progression))
        print(f"Question: {progression_str}")
        
        user_answer = input("Your answer: ").strip()
        try:
            user_answer_int = int(user_answer)
        except ValueError:
            user_answer_int = None
        
        if user_answer_int == correct_answer:
            print("Correct!")
        else:
            print(f"'{user_answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.")
            return False
    
    return True


def main():
    print("Welcome to the Brain Games!")
    name = input("May I have your name? ")
    print(f"Hello, {name}!")
    print("What number is missing in the progression?")
    
    if progression_game():
        print(f"Congratulations, {name}!")
    else:
        print(f"Let's try again, {name}!")
        

if __name__ == "__main__":
    main()
