from enum import Enum
import random
import sys

def welcome():
    start1 = "\n************************************************"
    start2 = "*                                              *"
    start3 = "*            Rock * Paper * Scissor            *"
    print(start1+'\n'+start2+'\n'+start3+'\n'+start2+'\n'+start1+'\n')

def rps(name="PlayerOne", arcade=False):
    [welcome() if not arcade else None]
    #welcome()

    game_count = 0
    player_wins = 0
    python_wins = 0

    def play_rps():
        nonlocal name
        nonlocal player_wins
        nonlocal python_wins

        class RPS(Enum):
            ROCK = 1
            PAPER = 2
            SCISSORS = 3

        playerChoice = input(
            f"\n{name}, Please enter ...\n1 for Rock\n2 for Paper\n3 for Scissors\n\nChoice: ")
        
        if playerChoice not in ['1', '2', '3']:
            print(f"{name}, please enter 1, 2, or 3.")
            return play_rps()
        player = int(playerChoice)

        computerChoice = random.choice('123')
        computer = int(computerChoice)

        print(f"\n{name}, you chose " + str(RPS(player).name) + ".")
        print("Python chose " + str(RPS(computer).name) + ".\n")

        def decide_winner(player, computer):
            nonlocal name
            nonlocal player_wins
            nonlocal python_wins

            if player == 1 and computer == 3:
                player_wins += 1
                return (f"🥳 {name} win!")
            elif player == 2 and computer == 1:
                player_wins += 1
                return (f"🥳 {name} win")
            elif player == 1 and computer == 3:
                player_wins += 1
                return (f"🥳 {name} win")
            elif player == computer:
                return ("🥹 It's a Tie!")
            else:
                python_wins += 1
                return (f"🐍 Python wins\nSorry, {name}...🥹")

        game_result = decide_winner(player, computer)

        print(game_result)

        nonlocal game_count
        game_count += 1
        
        print(f"\nGame count: {game_count}")
        print(f"\n{name} wins: {player_wins}")
        print(f"\nPython wins: {python_wins}")

        print(f"\nPlay again, {name}?")
        
        while True:
            playerAgain = input("\nY for yes or \nQ to Quit\n\nDecision: ")
            if playerAgain.lower() not in ['y', 'q']:
                continue
            else:
                break
            
        if playerAgain.lower() == 'y':
            return play_rps()
        else:
            if __name__ == "__main__":
                print("\n🥳🥳🥳🥳🥳🥳\nThank you for playing")
                sys.exit(f"\nBye {name}👋")
            else:
                return
    
    return play_rps

if __name__ == '__main__':

    import argparse

    parser = argparse.ArgumentParser(
        description="Provides a personal game experience"
    )
    # dest="firstName",
    parser.add_argument(
        "-n", "--name", metavar="name", required=False,
        help="The name of the person playing the game"
    )
    args = parser.parse_args()

    rock_paper_scissors = rps(args.name)
    rock_paper_scissors()