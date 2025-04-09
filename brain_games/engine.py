from brain_games.cli import welcome_user


def launch_game(game_module):
    name = welcome_user()
    print(game_module.DESCRIPTION)
    
    rounds = 3
    for _ in range(rounds):
        question, correct_answer = game_module.generate_round()
        print(f"Question: {question}")
        user_answer = input("Your answer: ").strip()
        if user_answer != str(correct_answer):
            print(f"'{user_answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {name}!")
            return
        else:
            print("Correct!")
    print(f"Congratulations, {name}!")
