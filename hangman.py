from words import palabras, vidas_pic
import random
import colorama 
from colorama import Fore,init
init()
colors = list(vars(colorama.Fore).values())#c paleta de colores

vidas = 0

def good_word(words):
        word = random.choice(words)
        while '-' in word or ' ' in word:
            word = random.choice(words)
        return word

print(Fore.CYAN +"\nBienvenido al juego del ahorcado: (;")
print(Fore.CYAN +"Esta es la palabra a adivinar\n")
word = good_word(palabras).upper()
word_list = list(word) #Separa las letras en una lista
count_letters = len(word_list) #Cantidad de letras a adivinar

while count_letters > 0 or vidas == 6:
    print(Fore.GREEN +"Adivina la palabra o frase")

    
    for i in word_list:
        if i.isupper():
            #print(" _ ",end="")
            colored_chars = [random.choice(colors)+ " _ " ]#random color
            print(" ".join(colored_chars),end="") #c 
            
        else:
            print(i,end="")

    print("")

    letter = input("\nPalabra: ").upper()
    if letter.isalpha() and len(letter) == 1:
        con = 0
        for i in range(len(word_list)):          
            if letter == word_list[i]:
                word_list[i] = letter.lower()
                con = con + 1
        if con == 0:
            vidas = vidas + 1 
        else:                
            count_letters = count_letters - con #letra menos           
            #print("Vamos bien, te faltan solamente ",count_letters)

        print(Fore.CYAN + vidas_pic[vidas])
        if vidas == 6:
            print(Fore.RED +"¡Has perdido!")
            print("La palabra era: ", word)
            break
            
        if count_letters == 0:
            print(Fore.GREEN +"¡Enhorabuena!, has ganado el juego del ahorcado")
            print(Fore.CYAN +"Palabra: ", word)
            
    else:
        print(Fore.YELLOW +"No reconoce este valor, intenta de nuevo")  
        print(Fore.YELLOW +"Aviso, solo puedes ingresar una letra")