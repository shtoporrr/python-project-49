import random
import math


def gcd_game():
    rounds = 3
    for _ in range(rounds):
        num1 = random.randint(1, 100)
        num2 = random.randint(1, 100)
        print(f"Question: {num1} {num2}")

        user_answer = input("Your answer: ").strip()

        correct_answer = math.gcd(num1, num2)

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
    print("Find the greatest common divisor of given numbers.")

    if gcd_game():
        print(f"Congratulations, {name}!")
    else:
        print(f"Let's try again, {name}!")


if __name__ == "__main__":
    main()
