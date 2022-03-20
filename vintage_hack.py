__author__ = 'MLadbrook'

import numpy as np
import random

random.seed(10)

words_four = ['help', 'dogs', 'cats', 'does', 'baby', 'burn', 'most', 'wake', 'want', 'good']
words_five = ['pleat', 'hello', 'tears', 'mouse']
words_six = []
words_seven = []
words_eight = []

x = 10
y = 20
number_of_words = 10

punctuation = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', ':', ';', '"',
               '{', '}', '[', ']', '+', '=', '?', '/', '>', '<', '~', '|', ',']

grid = np.full((x, y), '')

difficulty = int(input('Select difficulty (1,2,3,4,5): '))
diff_dict = {1: words_four, 2: words_five, 3: words_six, 4: words_seven, 5: words_eight}

words = random.sample(diff_dict[difficulty], number_of_words)
length_of_word = len(words[0])


used_coords = []


def check_coords(coord):
    if coord in used_coords:
        return True
    else:
        return False


def create_grid(x, grid):
    '''Create string version of grid'''
    for level in range(0, x):
        print(''.join(map(str, grid[level])))


def back_fill(array):
    '''Fill with random'''
    for (x, y), value in np.ndenumerate(array):
        if value:
            continue
        grid[x, y] = random.choice(punctuation)
    return grid


def create_index(array):
    counter = 1
    index = {}
    for (x, y), value in np.ndenumerate(array):
        index[counter] = x, y
        counter += 1
    return index


def check_word(answer, attempt):
    number_correct = 0
    to_check = answer
    for letter in attempt:
        if letter in to_check:
            number_correct += 1
            to_check = to_check.replace(letter, '')
    return number_correct


grid_index = create_index(grid)


def create_starting_points():
    starting_points = random.sample(range(len(grid_index) - length_of_word), len(words))
    starting_points.sort()
    diffs = [j-i for i, j in zip(starting_points[:-1], starting_points[1:])]
    #print(diffs)
    for i in diffs:
        if i < length_of_word + 1:
            return create_starting_points()
    return starting_points


starting_points = create_starting_points()

for item in range(len(words)):
    word = [letter for letter in words[item]]
    starting_point = starting_points[item]
    grid[grid_index[starting_point]] = word[0]
    for i in range(1, len(word)):
        grid[grid_index[starting_point + i]] = word[i]



back_fill(grid)
create_grid(x, grid)

answer = random.choice(words)
no_chances = 3
while no_chances > 0:
    guess = input('What word? ')
    if guess not in words:
        print('Invalid input. Retry.')
        continue
    if guess == answer:
        print('Access granted.')
        break
    else:
        print('Number of correct letters: {}'.format(check_word(guess, answer)))
        no_chances -= 1
        if no_chances == 0:
            print('Self destruct initiated.')



