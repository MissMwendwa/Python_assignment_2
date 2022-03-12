import random


words = ['holiday', 'american', 'restaurant', 'computer', 'highschool', 'programming']
random_word = random.choice(words)
count = 0


while True:                                     #repeatedly asks you to guess the letter in a random word
    guess = str(input("Guess a letter:  "))
    guess = guess.lower()


    if guess in random_word:             #checks if the letter you input is in the random generated word
        print("Yay, its in the word")
      
    
    else:                          
        count += 1
        print("Not in the word, attempts: %d" % count)
        
        if count > 5:                   
            print("You have reached max attempts")
            print("Sorry, but hangman died! You lose")
            break
        else:
            continue