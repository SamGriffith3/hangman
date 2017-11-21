def setup():
  player_1 = input("What's your name Player 1? : ")
  print("Nice to meet you " + player_1)
  player_2 = input("How about your name Player 2? : ")
  print("Suck it " player_2)

  
turn = 0
guess_number = 5
word_length = len(word)
round_limit = Input("Number of Rounds: ")

def chair_1(round_limit):
  while round_limit > 0:
      print("You have __ rounds left!") (round_limit)


def run():
  chair_1(round_limit)
  return round_limit - 1
  
  
def round(turn):
  win_count_1 = 0
  win_count_2 = 0
  while guess_number > 0 and sum(win_count_1, win_count_2) < 5:  
      if turn == 0:
        player_A = player_1
        player_B = player_2
      else:
        player_A = player_2
        player_B = player_1
      word = input(player_A + ", what's the word? : ") 
      print("You have put in a " + word_length + " letter word!")
      chars = []
      guessed_chars = []
      correct_chars = []
      for i in word:
         chars.append(i)
         correct_chars.append("_")
         g = Input("What's your guess " + player_B)
         guessed_chars.append(g)
         print("So far, you have guessed " + guessed_chars)
         if g in word:
             letter_count = word.count(g)
             print g + "is in" + word + " " letter_count " times!"
             for g in word:
                 loc = word.index(g)
                 correct_chars[loc] = g
                 guess_number -= 1
                 print(correct_chars)
                 total_letters = total_letters + letter_count
                 if total_letters == word_length:
                     print ("Congrats! You found all the letters for " + word)
                     turn += 1  
                     if turn == 0:
                        win_count_1 += 1
                     else:
                        win_count_2 += 1
                     print(player_1 " has won " + win_count_1 + " rounds! And " + player_2 + " has won " + win_count_2 + " rounds!" 
                 else:
                     guess_number -= 1
                     print("You have " + guess_number + " guesses left! Keep it up!")
         else:
             print(g + "is not in " + word)
             guess_number -= 1
  elif sum(win_count_1, win_count_2) == 5:
     if win_count_1 > win_count_2:
        print(player_1 + " wins!!!)
     else:
        print(player_2 + " wins!!!)
                           
  else:
    print "uh-oh"
    if turn == 0:
        print(player_2 + "has run out of turns")
        turn += 1
        guess_number = 5
    else:
        print(player_1 + "has run out of turns")
        turn -= 1
        guess_number = 5

#Execute the program        
setup() 
round(0) 
