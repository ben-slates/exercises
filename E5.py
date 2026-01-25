import random

while True:
    choice = (0, 1, 2)
    computer = random.choice(choice)
    rules = [
        ["D", "W", "L"],  
        ["L", "D", "W"],  
        ["W", "L", "D"]   
    ]
    player = int(input(
        "Please select your number:\n"
        "0. Snake\n"
        "1. Water\n"
        "2. Gun\n"
        "Enter: "
    ))
    if player < 3 :
        result = rules[player][computer]
        print(f"Computer chose: {computer}")

        if result == "W":
            print("Player wins")
        elif result == "L":
            print("Player loses")
        else:
            print("Draw")
    else:
        print("wrong input!")
    play_again = input("Play again? (y/n): ").lower()

    if play_again != "y":
        break
