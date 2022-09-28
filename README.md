# Hangman_game
<figure>
<div style="text-align:center"><img src="hangman.png" alt="Hangman" width="100" heiht="100">
<span><figcaption>fig1: In this round, 'M' should be guessed "Co_puter" but guessed letter "a" </figcaption><span>
</div>
</figure>

> ## How to Play this ??
Hangman game is a simple word guessing game. It played with two or more people. One person will play a major role as a host and will think of a word  as another one is responsible to guess and find out the hidden word. In each guess, if an alphabet occurs in the hidden word then the host will fill with the character. If not then the host will draw a part of the body.  if all blanks are revealed the person wins the game. If the hangman's part is completely revealed the player loses the game.  

 **Milestone1:** 
---

### 1. **Create the variables for the game**
- Create the list containing the name of your favorite fruits
- Get the output by using the print() in-built function.
- random.choice() method used for randomly choosing the one word from the list. 
- "_ _ name_ _ == _ _ main_ _" is used to execute some code only if the file runs directly, and is not imported
- Character checking evaluates alphabetic letters, which length should be one. 

**Milestone2:** 
--- 
### 2. **Check if the guessed character is in the word**
 -  ### I used two functions for this task.
    - check_guess(): Check the character present in the randomly chosen word.
    - ask_for_input() : 
        * If the guessed letter is valid with the condition, the function will be checked whether the character occurs in the word.
        * If the guessed letter is not valid it will repeat the loop until getting the valid input. 
