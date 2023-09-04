import sys
import guess_number
import rps

welcome_screen = """
************************************************
*                                              *
*           WELCOME TO THE ARCADE              *
*                                              *
************************************************
"""
print(welcome_screen)


def game_mode(name='PlayerOne'):

    print(f"\n{name}, welcome to the Arcade! 😀")

    def game_preference():
        nonlocal name
        GAMES = {
            "rps": rps.rps(name, True),
            "gmn": guess_number.guess_number(name, True)
        }

        print("\nPlease choose a game:")
        print("1 = Rock Papar Scissors\n2 = Guess My Number\n\nOr press \"x\" to exit the Arcade")

        choice = input("\nGame: ")

        if choice[0].upper() == 'X':
            sys.exit(f"\n🎇🎇🎇🎇🎇\nThanks for visiting the Arcade\n\nBye {name}! 👋")

        if choice not in ['1', '2']:
            print(f"\n{name}, please enter 1, 2 or x.")
            game_preference()

        if choice == '1':
            initiate = GAMES["rps"]
            initiate()
            print(f"\n{name}, welcome back to the Arcade! 😀")
            game_preference()
        else:
            initiate = GAMES["gmn"]
            initiate()
            print(f"\n{name}, welcome back to the Arcade! 😀")
            game_preference()

    return game_preference

if __name__ == '__main__':
  import argparse
  
  parser = argparse.ArgumentParser(
    description="This is an Arcade game selector"
  )
  parser.add_argument(
    '-n', '--name', metavar='name', required=True, 
    help="The name of the person playing the game"
  )
  args = parser.parse_args()

  game_console = game_mode(args.name)
  game_console()