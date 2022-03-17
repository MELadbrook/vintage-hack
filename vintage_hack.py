__author__ = 'MLadbrook'

import numpy as np
import random

words_four = {'help', 'dogs', 'cats', 'does'}
words_five = {'pleat', 'hello', 'tears', 'mouse'}

x = 10
y = 20
number_of_words = 2

punctuation = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', ':', ';', '"',
               '{', '}', '[', ']', '+', '=']

grid = np.full((x, y), '')

words = random.sample(words_five, number_of_words)
print(words)

used_coords = []


def check_coords(coord):
    if coord in used_coords:
        return True
    else:
        return False


def create_grid(x, grid):
    '''Create string version of grid'''
    for level in range(1, x):
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


grid_index = create_index(grid)


#print(back_fill(grid))
#create_grid(x, grid)

print("Character from grid: {}".format(grid[grid_index[0]]))


for item in words:
    word = [letter for letter in item]
    starting_point = random.randint(0, len(grid_index) - len(word))
    grid[grid_index[starting_point]] = word[0]
    for i in range(1, len(word)):
        grid[grid_index[starting_point + i]] = word[i]


print(grid)
'''
for word in words:
    word = [letter for letter in word]
    starting_point = (random.randint(0, x-1), random.randint(0, y-1))
    grid[starting_point] = word[0]
    used_coords.append([starting_point[0], starting_point[1]])
    break_point = 0
    for i in range(1, len(word)):
        try:
            grid[starting_point[0], starting_point[1] + i] = word[i]
            used_coords.append([starting_point[0], starting_point[1] + i])
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
                used_coords.append([starting_point[0] + 1, 0 + i])
            except IndexError:
                print("System Error: Please attempt again.")
                break'''
