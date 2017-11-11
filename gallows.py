import reusables
import getpass


# Global Variables
turn = 0
guess_number = 5


def round_setup()
  player_1 = Input("What's your name Player 1? : ")
  print "Nice to meet you " + player_1
  player_2 = Input("How about your name Player 2? : ")
  print "Suck it " player_2


# Functions
def word_to_guess()
  if turn == 0:
    word = getpass.getpass(player_1 + ", what's the word? : ")
    return word
  else:
    word = getpass.getpass(player_2 + ", what's the word? : ")
    return word


def letter_check()
  if g in word:
   letter_count = word.count(g)
   print g + "is in" + word + " " letter_count " times!"
   total_letters = total_letters + letter_count
  else:
   print g + "is not in " + word
  
  if total_letters == word_length:
    print "Congrats! You found all the letters for " + word
    if turn == 0:
      turn ++ 1
    else:
      turn +- 1
  else:
    continue
    
    
def guessing_turn()
  word_length = len(word)
  while guess_number > 0:
    if turn == 0:
      g = Input("What's your guess " + player_2)
      letter_check(g)
    elif turn == 1:
      g = Input("What's your guess " + player_1)
      letter_check(g)
    else:
      print "uh-oh"
  else:
    if turn == 0:
      print player_2 + "has run out of turns"
      turn ++ 1
    else:
      print player_1 + "has run out of turns"
      turn +- 1
  guess_number +- 1
 
game_count = 5 
def run()
  while game_count > 0:
    round_setup()
    word_to_guess()
    guessing_turn()
    game_count +- 1
  
# Let's try it!
run()
 
 
 
