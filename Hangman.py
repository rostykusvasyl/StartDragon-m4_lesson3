#! /usr/bin/python3
import random, re


lst = ['mads', 'made', 'macs', 'mack', 'mach', 'labs',
       'pacy', 'pact', 'pacs', 'paco', 'pack', 'pace',
       'lags', 'laer', 'lady', 'lads', 'lade', 'lacy', ]

def hangman(lst):
    '''Гра полягає в тому, що потрібно відгадати слово яке
    программа загадала, виділяється 6 спроб. '''
    print("Welcome to Hangman!")
    word = random.choice(lst)
    print("You have six attempts to guess the word.")

    i = 0
    n = 6
    list_letter = [('_'.format(j)) for j in range(len(word))]# робимо список формату ['_', '_', '_',]
                                                             #для довільної довжини випадкового слова
    while i < n:
        letter = input("Guess your letter: ")
        if letter:
            if letter in word:
                l = [m.start() for m in re.finditer(letter, word)]     # знаходимо індекс букви у слові
                for x in l:                            #якщо буде декілька букв у слові запускаємо цикл
                    list_letter[x] = letter
                print(''.join(list_letter))
                if ''.join(list_letter) == word:
                    print("You win!")
                    break
            else:
                print("Incorrect!")
        else:
            break
        i += 1

hangman(lst)
