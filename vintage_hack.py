__author__ = 'MLadbrook'

import numpy as np
import random

words_four = {'help', 'dogs', 'cats', 'does', 'baby', 'burn', 'most', 'wake', 'want', 'good'}
words_five = {'pleat', 'hello', 'tears', 'mouse'}

x = 10
y = 20
number_of_words = 10

punctuation = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', ':', ';', '"',
               '{', '}', '[', ']', '+', '=']

grid = np.full((x, y), '')

words = random.sample(words_four, number_of_words)
length_of_word = len(words[0])
print(words)

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
        #print('\n')


def back_fill(array):
    '''Fill with random'''
    for (x, y), value in np.ndenumerate(array):
        if value:
            continue
        grid[x, y] = random.choice(punctuation)
    return grid


def create_index(array):
    counter = 0
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


#print(back_fill(grid))
#create_grid(x, grid)

#print("Character from grid: {}".format(grid[grid_index[0]]))



#starting_points = random.sample(range(len(grid_index)-(len(words)-1)*(length_of_word)+1), len(words))
#starting_points = np.cumsum(np.ones((len(words),), np.int) * (length_of_word+1) + np.random.randint(0, 200, (len(words),))) - (length_of_word+1)




def create_starting_points():
    starting_points = random.sample(range(len(grid_index)), len(words))
    starting_points.sort()
    diffs = [j-i for i, j in zip(starting_points[:-1], starting_points[1:])]
    print(diffs)
    for i in diffs:
        if i < length_of_word + 1:
            return create_starting_points()
    return starting_points


starting_points = create_starting_points()

for item in range(len(words)):
    word = [letter for letter in words[item]]
    starting_point = starting_points[item]
    #for point in starting_points:
     #   if starting_point - point < len(word) | starting_point - point != 0:


    grid[grid_index[starting_point]] = word[0]
    for i in range(1, len(word)):
        grid[grid_index[starting_point + i]] = word[i]


print(grid)
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



