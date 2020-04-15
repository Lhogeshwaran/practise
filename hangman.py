# HANGMAN CHALLENGE

import random
import sys

words = ['placebo', 'earth', 'sanity', 'python']

word = random.choice(words)

blanks = ['_' for i in range(len(word))]

peding_guess = 8

print('Welcome to hangman!')
print(f'Your word looks like this {" ".join(blanks)}')
print('You have 8 guesses left.')

while peding_guess >= 0:

  guess = input('Enter your guess...')

  if guess in word and peding_guess > 0:
    blanks[word.index(guess)] = guess
    print('Your guess is correct.')
    print(f'Your word now looks like this {" ".join(blanks)}')
    if '_' not in blanks:
      print('You win!! Congratualtions')
      break
    print(f'You still have {peding_guess} guesses left.')
    continue

  elif guess not in word and peding_guess > 0:
    print('Your guess is incorrect.')
    peding_guess -= 1
    print(f'Your word now looks like this {" ".join(blanks)}')
    print(f'You now have {peding_guess} guesses left.')
    continue

  else:
    (print('Game over!\nYou do not have any more guesses left!'))
    break
