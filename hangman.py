# Import modules to use
from words import palabras
from colorama import Fore,Style, init
init()
import random


print("Welcome to the game hangman in Python!! ")

def key_word(palabras):
  word = random.choice(palabras)

  while '-' in word or ' ' in word: 
    word = random.choice(palabras)
  return word


for i in key_word(palabras):
    print(Fore.RED + " _ ",end="")
print("")



