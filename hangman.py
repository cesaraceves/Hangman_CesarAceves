# Import modules to use
from words import palabras
import random


print("Welcome to the game hangman in Python!! ")

def key_word(palabras):
  word = random.choice(palabras)

  while '-' in word or ' ' in word: 
    word = random.choice(palabras)
  return word


for i in key_word(palabras):
    print(" _ ",end="")
print("")



