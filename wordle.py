#wordle.py
import pathlib
import random 
from string import ascii_letters
from rich import print, Console

console = Console(width=40)
def get_random_word():

    wordlist = pathlib.Path(__file__).parent/"words.txt"
    words = [word.upper() for word in wordlist.read_text(encoding='utf-8').strip().split('\n')
    if len(word) == 5 and all(letter in ascii_letters for letter in word )]
   
    word = random.choice(words)
    return word

def show_guess(word, guess):
    if guess == word:
        print('Correct') 
    correct = {letter for letter, correct in zip(guess, word) if letter == correct}
    wrong = set(guess)- set(word)
    misplaced = set(guess) & set(word) - correct
    print("These letters are correct" , ''.join(sorted(correct)))
    print("These letters are", ''.join(sorted(wrong)))
    print("These misplaced letters are", ''.join(sorted(misplaced)))


def game_over(word):
    print(f'the word was {word}')

def main():
    word = get_random_word()
    guesses =["_"*5]*6
    for idx in range(6):
        guesses[idx]  = input(f'\n guess the word').upper()
        show_guess(word, guesses[idx])
        if guesses[idx] == word:
            print('correct')
    game_over(word)

def refresh_page(headline):
    console.clear()
    console.rule(f'')

if __name__ == '__main__':
    main()