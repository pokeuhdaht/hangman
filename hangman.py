#           HANGMAN



import random

Fruits = """apple pear peach banana mango """

fruits=Fruits.split(' ')
word = random.choice(fruits)



print("Guess the Fruit!")
print("You get 5 strikes")

correct= False
strikes=5
while strikes !=0 and correct==False:

    for i in word:
        print("_",end=" ")
        continue

    passGuess=False
    while passGuess==False:
        guess=input("\nEnter a letter to guess: ")
        if not guess.isalpha():
            print("Please enter a letter.")
        elif len(guess) > 1:
            print("Please enter only one letter.")
       # elif guess in lettersGuessed:
        #    print("Letter has already been used")

        
    
                

    

    

            
