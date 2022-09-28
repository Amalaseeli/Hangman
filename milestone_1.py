import random
word_list=['Apple','Banana','Grape','Stawberry','Peach']
#print(word_list)
word=random.choice(word_list)
#print(word)
guess=input('Enter a single letter:')
#Check the user input a alphabetical character 
if len(guess)==1 and guess.isalpha():
    print('Good guess')
else:
    print('Oops! That is not a valid input.')

