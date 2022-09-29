import random
import milestone_1 as m1

class Hangman():
    def __init__(self,word_list,num_lives=5):
        self.word=random.choice(word_list)
        self.word_guessed=[]
        self.num_letters=()
        self.num_lives=num_lives
        self.word_list=word_list
        self.list_of_guesses=[]
    
    def check_guess(self,guess):
        guess=guess.lower()
        print(self.word)
        if guess in self.word:
             print(f"Good guess! {guess} is in the word ")
        else:
            pass
    
    def ask_for_input(self):
         while True:
            guess=input("Guess the letter:")
            if  len(guess)>1 and guess.isalpha():
                print("Invalid letter. Please, enter a single alphabetical character.")
            elif guess in self.list_of_guesses:
                print("You already tried that letter!")
            else:
                self.check_guess(guess) 
                self.list_of_guesses.append(guess)
                print(self.list_of_guesses)


h1=Hangman(m1.word_list)   
h1.ask_for_input() 