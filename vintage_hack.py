__author__ = 'MLadbrook'

import numpy as np
import random

words_four = {'help', 'dogs', 'cats', 'does'}
words_five = {'pleat', 'hello', 'tears', 'mouse'}

x = 10
y = 8
number_of_words = 2

punctuation = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')']

grid = np.full((x, y), '')

words = random.sample(words_five, number_of_words)
print(words)





for word in words:
    word = [letter for letter in word]
    starting_point = (random.randint(0, x-1), random.randint(0, y-1))
    grid[starting_point] = word[0]
    break_point = 0
    for i in range(1, len(word)):
        try:
            grid[starting_point[0], starting_point[1] + i] = word[i]
        except IndexError:
            #grid[starting_point[0] + 1, [0]] = word[i]
            break_point = i
            print(break_point)
            word = word[break_point:]
            break
    if break_point > 0:
        for i in range(0, len(word)):
            try:
                grid[starting_point[0] + 1, [0 + i]] = word[i]
            except IndexError:
                print("System Error: Please attempt again.")
                break

print(grid)