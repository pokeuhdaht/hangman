#           HANGMAN Game



import random

Fruits = """apple pear peach banana mango"""

fruits=Fruits.split(' ')
word = random.choice(fruits)

print("Guess the Fruit!")
print("You get 5 strikes")

                #prints the number of letters from word identifiable by '_'
for i in word:
        print("_",end=" ")
        continue
    
correct= False                               #Flag to show whether word is correctly guessed
strikes=5                                  #identifies number of incorrect attempts, once this reached 0 game is over
lettersGuessed=''                        #creates a string that acts as a list for guessed characters
while strikes >0 and correct==False:
    letterCount=0

                        #determines whether or not the character input is valid
    passGuess=False
    while passGuess==False:
        guess=input("\nEnter a letter to guess: ")
        if not guess.isalpha():
            print("Please enter a letter.")
        elif len(guess) > 1:
            print("Please enter only one letter.")
        elif guess in lettersGuessed:
            print("Letter has already been used")
        else:
            lettersGuessed=lettersGuessed+guess
            passGuess=True


    print("Letters Used: "+lettersGuessed)          # . . . 

                        #prints letters in correct spot
    for j in word:
        if j in lettersGuessed:
            for k in lettersGuessed:
                if j in k:
                    print(j,end=" ")
                    letterCount+=1
                else:
                    continue
        else:
            print("_",end=" ")
    print()

    if guess not in word:
        strikes=strikes-1

    if letterCount==len(word):
        correct=True
        continue
        
    print("Number of strikes remaining: " + str(strikes))


print()

if correct==True:
    print("Congratulations you got the word right in " + str(len(lettersGuessed))+" attempts.")
else:
    print("Aww, you lost. Better luck next time!")


exit()        
    
                

    

    

            
