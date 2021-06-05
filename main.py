import random
import os

def get_word():
  with open("words.txt", "r") as f:
    words=f.read()
  words = words.split()
  word=random.choice(words)
  return word.upper()

def draw_hangman(attempts_wrong,ques,comment):
  new_str=""
  new_str+= ("     ------\n")
  new_str+= ("     |    |\n")
  new_str+= ("     |    " + ("O\n" if attempts_wrong > 0 else "\n"))
  new_str+= ("     |   " + ("/|\\\n" if attempts_wrong > 1 else "\n"))
  new_str+= ("     |    " + ("|\n" if attempts_wrong > 2 else "\n"))
  new_str+= ("     |   " + ("/ \\\n" if attempts_wrong > 3 else "\n"))           
  new_str+= (" --------- \n")
  new_str+=(ques)+ "\n"
  new_str+=(comment)+"\n"
  return new_str

def hangman():
  play=True
  while play:
    word = get_word()
    attempts_wrong=0
    letters=set(word)
    guessed_letters=[]
    ques="_ "*len(word)
    guessed= False
    comment =''
    while not guessed:
      os.system("clear") 
      print(draw_hangman(attempts_wrong,ques,comment))
      user=input("Enter a letter: ").upper()
      if len(user)==1:
        if user in guessed_letters:
          comment =  "You already guessed " + str(user) + ". Try again!"
        else:
          guessed_letters.append(user)
          new_ques =''
          if user in letters:
            comment = "Good guess, " + str(user) + " is in the word."
            for i, el in enumerate(word):
              if el==user or el in guessed_letters:
                new_ques += el + " "
              else:
                new_ques += '_ '
            ques = new_ques
          else:
            comment =  "You made the wrong guess.Try again!" 
            attempts_wrong+=1
      else:
        comment = "You can only make 1 guess at a time."
      if attempts_wrong > 3:
        comment = "You Lost!" 
        os.system("clear")
        print(draw_hangman(attempts_wrong,ques,comment))
        again=input("Do you want to play again? (Y/N)").upper()
        if again != 'Y':
          play =False
        guessed = True
      if "_" not in ques:
        guessed = True
        comment =   "Well done! You guessed the word."
        os.system("clear")
        print(draw_hangman(attempts_wrong,ques,comment))
        again=input("Do you want to play again? (Y/N)").upper()
        if again != 'Y':
          play =False
        
        
      
      


#if __name__ == "__main__": 
  #hangman() 


def test_hangman():
  print("Test cases")
  a=draw_hangman(0,"_ _ _ _ A", "Well done!")
  assert a=="""     ------
     |    |
     |    
     |   
     |    
     |   
 --------- 
_ _ _ _ A
Well done!
""", a

  b=draw_hangman(3, "_ _ _ _ _ _ _ _", "You Lost!")
  assert b=="""     ------
      |    |
      |    O
      |   /|\
      |    |
      |   
  --------- 
  _ _ _ _ _ _ _ _ 
  You Lost!
  """, b
test_hangman()