import random
import sys

def welcome():
  welcome_screen = """\n
  *************************************************
  *                                               *
  *               GUESS MY NUMBER                 *
  *                                               *
  *************************************************
  """
  print(welcome_screen)

def guess_number(name="PlayerOne", arcade=False):
  [welcome() if not arcade else None]
  #welcome()

  line = "**************************************************"
  game_count = 0
  player_wins = 0
  
  def start_game():
    nonlocal line
    nonlocal game_count
    nonlocal player_wins
    nonlocal name

    print(f"\n{name}, guess which number I'm thinking of... 1, 2, or 3")
    player_guess = input("\nYour Guess: ")
    computer_random_number = random.choice('123')

    if player_guess not in ['1', '2', '3']:
      print(f"{line}\n{name}, please enter 1, 2, or 3.\n{line}")
      return start_game()
    
    game_count += 1

    print(f"\n{name}, you chose {player_guess}")
    print(f"I was thinking about the number {computer_random_number}")
    
    if player_guess == computer_random_number:
      player_wins += 1
    else:
      print(f"\nSorry, {name}. Better luck next time")
    
    print(f"\nGame count: {game_count}")
    print(f"\n🥳 {name}'s wins: {player_wins}")
    print(f"\nYour winning percentage: {(player_wins / game_count):.2%}")
    
    print(f"\nPlay again, {name}?")
    print("\nY for Yes or\nQ to Quit")
    decision = input("\nDecision: ")

    if decision[0].upper() == 'Y' :
      start_game()
    else:
      if __name__ == "__main__":
        sys.exit(f"\n🎇🎇🎇🎇🎇\nThanks for playing\n\nBye {name}! 👋")
      else:
        return
  
  return start_game

if __name__ == "__main__":
  
  import argparse

  parser = argparse.ArgumentParser(
    description="This is a game in which the user guesses the number"
  )
  parser.add_argument(
    '-n', '--name', metavar='name', required=True, 
    help="The name of the person playing the game"
  )
  args = parser.parse_args()

  game_console = guess_number(args.name)
  game_console()