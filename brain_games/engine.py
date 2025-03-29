def launch_game(game_module):
    print("Welcome to the Brain Games!")
    name = input("May I have your name? ")
    print(f"Hello, {name}!")
    print(game_module.DESCRIPTION)
    
    if game_module.play_rounds():
        print(f"Congratulations, {name}!")
    else:
        print(f"Let's try again, {name}!")
