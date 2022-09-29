import random
import milestone_1 as m1

class Hangman():
    def __init__(self,word_list,num_lives=5):
        self.word=random.choice(word_list)
        self.word_guessed=[]
        self.num_letters=len(set(self.word))
        self.num_lives=num_lives
        self.word_list=word_list
        self.list_of_guesses=[]
    
    def check_guess(self,guess):
        word_guessed=guess.lower()
        print(self.word)
        #if word_guessed is in the word
        if  word_guessed in self.word:
            print(f"Good guess! {word_guessed} is in the word ")
            for letter in self.word:
                if letter==word_guessed:
                    word_guessed=letter
                    print("you achieved")
            self.num_letters-=1
        #if word_guessed is not in the word
        else:
            self.num_lives-=1
            print(f"Sorry, {word_guessed} is not in the word")
            print(f"You have {self.num_lives} lives left.")
        self.list_of_guesses.append(word_guessed)
    
    def ask_for_input(self):
         while True:
            guess=input("Guess the letter:")
            if  len(guess)>1 or not guess.isalpha():
                print("Invalid letter. Please, enter a single alphabetical character.")
            elif guess in self.list_of_guesses:
                print("You already tried that letter!")
            else:
                self.check_guess(guess) 
                self.list_of_guesses+=guess
                #print(self.list_of_guesses)


h1=Hangman(m1.word_list)   
h1.ask_for_input() 