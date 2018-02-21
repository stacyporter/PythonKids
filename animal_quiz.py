def check_guess(guess,answer):
    global score
    if guess == answer:
        print('Correct answer')
        score = score + 1

score = 0
print('Guess the animal!')
guess1 = input('Which bear lives at the North Pole? ')
check_guess(guess1,'polar bear')
guess2 = input('Which is the fastest land animal? ')
check_guess(guess2,'cheetah')
guess3 = input('Which is the largest animal? ')
check_guess(guess3,'blue whale')

print('You score is ' + str(score))
