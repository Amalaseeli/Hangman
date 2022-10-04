import random

''' A Hangman Game that asks the user for a letter and checks if it is in the word.
    It starts with a default number of lives and a random word from the word_list. '''

'''
     Parameters:
    ----------
    word_list: list
        List of words to be used in the game
    num_lives: int
        Number of lives the player has
    
    Attributes:
    ----------
    word: str
        The word to be guessed picked randomly from the word_list
    word_guessed: list
        A list of the letters of the word, with '_' for each letter not yet guessed
        For example, if the word is 'apple', the word_guessed list would be ['_', '_', '_', '_', '_']
        If the player guesses 'a', the list would be ['a', '_', '_', '_', '_']
    num_letters: int
        The number of UNIQUE letters in the word that have not been guessed yet
    num_lives: int
        The number of lives the player has
    list_of_guesses: list
        A list of the letters that have already been tried
        
    Methods:
    -------
    check_letter(letter)
        Checks if the letter is in the word.
    ask_letter()
        Asks the user for a letter.
    '''
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
        '''
        Checks if the guess is in the word.
        If it is, it replaces the '_' in the word_guessed list with the guess.
        If it is not, it reduces the number of lives by 1.
        Parameters:
        '''
       #if word_guessed is in the word
        if  guess in self.word:
            print(f"Good guess! {guess} is in the word ")
            for i,letter in enumerate(self.word):
                if guess==letter:
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
        '''
        Asks the user for a letter and checks:
        1. If the letter has already been tried
        2. If the character is a single character
        If it passes both checks, it calls the check_guess method.
        '''
        while True:
            guess=input("Guess the letter:")
            if  len(guess)>1 or not guess.isalpha():
                print("Invalid letter. Please, enter a single alphabetical character.")
            elif guess in self.list_of_guesses:
                print("You already tried that letter!")
            else:
                self.check_guess(guess)
                break

def play_game():
    num_lives=input("Enter the number of lives you wish to play:")
    word_list=['Apple','Banana','Grape','Strawberry','Peach']
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
   
if __name__=="__main__":
    play_game()
        


