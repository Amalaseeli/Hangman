import random
import milestone_1 as m1

class Hangman():
    def __init__(self,word_list,num_lives=5):
        self.word=random.choice(word_list).lower()
        self.num_letters=len(set(self.word))
        self.word_guessed=len(self.word)*["_"]
        self.num_lives=int(num_lives)
        self.word_list=word_list
        self.list_of_guesses=[]
    
    def check_guess(self,guess):
        guess=guess.lower()
        print(self.word)
        
        #if word_guessed is in the word
        if  guess in self.word:
            print(f"Good guess! {guess} is in the word ")
            for i,letter in enumerate(self.word,start=0):
                
                 if guess==letter:#Look at the enumerate function here.
                    print("you achieved")
                    self.word_guessed[i]=guess
                    print(self.num_letters)
            self.num_letters-=1
                    
                        
        #if word_guessed is not in the word
        else:
            self.num_lives-=1
            print(f"Sorry, {guess} is not in the word")
            print(f"You have {self.num_lives} lives left.")
        self.list_of_guesses.append(guess)

        print(self.word_guessed)
    
    def ask_for_input(self):
         while True:
            guess=input("Guess the letter:")
            if  len(guess)>1 or not guess.isalpha():
                print("Invalid letter. Please, enter a single alphabetical character.")
            elif guess in self.list_of_guesses:
                print("You already tried that letter!")
            else:
                
                self.check_guess(guess) 
                #print(self.list_of_guesses)
                #self.list_of_guesses+=guess
                
                break


def play_game():
    num_lives=input("Enter the number of lives you wish to play:")

    word_list=['Apple','Banana','Grape','Stawberry','Peach']
    game=Hangman(word_list,num_lives)
    while True:
        if game.num_lives==0:
            print("You lost")
            break
        elif game.num_letters>0:
            game.ask_for_input()
        elif game.num_lives!=0 and game.num_letters==0:
            print("Congratulations! You won the game.")
            break
#h1=Hangman(m1.word_list)   

play_game()
        


