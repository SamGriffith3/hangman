

def round()
  player_1 = input("What's your name Player 1? : ")
  print("Nice to meet you " + player_1)
  player_2 = input("How about your name Player 2? : ")
  print("Suck it " player_2)

  turn = 0
  guess_number = 5
  word_length = len(word)
   
      
  while guess_number > 0:
    if turn == 0:
       word = input(player_1 + ", what's the word? : ") # I want to find a way to hide the word from the console after it is inputted
       print("You have put in a " + word_length + " letter word!")
       chars = []
       guessed_chars = []
       correct_chars = []
       for i in word:
          chars.append(i)
          correct_chars.append("_")
          g = Input("What's your guess " + player_2)
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
                  else:
                      guess_number -= 1
                      print("You have " + guess_number + " guesses left! Keep it up!")
            else:
                print(g + "is not in " + word)
                guess_number -= 1
    elif turn == 1:
       word = input(player_2 + ", what's the word? : ")
       print("You have put in a " + word_length + " letter word!")
       chars = []
       guessed_chars = []
       correct_chars = []
       for i in word:
          chars.append(i)
          correct_chars.append("_")
          g = Input("What's your guess " + player_1)
          guessed_chars.append(g)
          print("So far, you have guessed " + guessed_chars)
          if g in word:
              letter_count = word.count(g)
              print g + "is in" + word + " " letter_count " times!"
              for g in word:
                  loc = word.index(g)
                  correct_chars[loc] = g
                  print(correct_chars)
                  total_letters = total_letters + letter_count
                  if total_letters == word_length:
                      print ("Congrats! You found all the letters for " + word)
                      turn -= 1
                      guess_number = 0
                  else:
                      guess_number -= 1
                      print("You have " + guess_number + " guesses left! Keep it up!")
        else:
            print(g + "is not in " + word)
            guess_number -= 1 
  else:
    print "uh-oh"
    if turn == 0:
        print(player_2 + "has run out of turns")
        turn += 1
    else:
        print(player_1 + "has run out of turns")
        turn -= 1
  
  
round() 




  
  
    
 
 
 
