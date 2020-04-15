# HANGMAN CHALLENGE

import random
import sys
import os

# words = ['placebo', 'earth', 'sanity', 'python']

f = open(os.path.join(os.getcwd(), 'data_files/hangman_words.txt'), 'r')
words = [l.strip('\n') for l in f]
f.close()

word = random.choice(words)

blanks = ['_' for i in range(len(word))]

peding_guess = 8

guessed_words = set()

print('Welcome to hangman!')
print(f'Your word looks like this {" ".join(blanks)}')
print('You have 8 guesses left.')

while peding_guess >= 0:

  if peding_guess > 0:
    guess = input('Enter your guess...')[0]
    if guess in guessed_words:
      print('Word already entered.')
      print(f'Entered words ... {"-".join(sorted(list(guessed_words)))}')
      print(f'Your word now looks like this {" ".join(blanks)}')
      print(f'You still have {peding_guess} guesses left.')
      continue
    guessed_words.add(guess)

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
    (print(f'Game over!\nYou do not have any more guesses left!\nThe word was "{word}".'))
    break
