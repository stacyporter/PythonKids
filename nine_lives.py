import random
import string

lives = 9
words = ['sleepy','slow','smelly',
         'wet','fat','red',
         'orange','yellow','green',
         'blue','purple','fluffy',
         'white','proud','brave',
         'apple','dinosaur','ball',
         'toaster','goat','dragon',
         'hammer','duck','panda',
         'footy','endzone','blitz']
word = random.choice(words)
reveal = []
guessed = False
for i in range(0,len(word)):
    reveal.append('*')
print('The word is ' + word)
while lives != 0 and guessed != True:
    print('Secret word: ' + str(reveal))
    print('Lives remaining: ' + str(lives))
    response = input('Guess a letter or word:')
    if len(response) == 1:
        if word.find(response) == -1:
            print('Incorrect letter')
            lives = lives - 1
        else:
            print('Correct letter')
            found = 0
            while word.find(response,found) != -1:
                reveal[word.find(response,found)] = response
                found = word.find(response,found)
    else:
        if response == word:
            print('Congratulations! You guessed the word')
            guessed = True
print('Game over! The word was ' + word)
                
                
                
