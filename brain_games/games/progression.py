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


def generate_round():
    progression, correct_answer = generate_progression()
    question = " ".join(map(str, progression))
    return question, correct_answer
