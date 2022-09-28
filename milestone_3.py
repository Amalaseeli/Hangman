import random
import milestone_1 as m1

class Hangman():
    def __init__(self,word_list,num_lives=5):
        word=random.choice(m1.word_list)
        