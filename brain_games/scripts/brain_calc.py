import random


def calc_game():
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
        elif op == '*':
            correct_answer = num1 * num2

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
    print("What is the result of the expression?")

    if calc_game():
        print(f"Congratulations, {name}!")
    else:
        print(f"Let's try again, {name}!")


if __name__ == "__main__":
    main()

