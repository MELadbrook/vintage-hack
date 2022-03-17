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
                break


#print(grid)
#print('\n\n\n')
#print(used_coords)
#print(''.join(map(str, grid[0])))


def create_grid(x, grid):
    for level in range(1, x):
        print(''.join(map(str, grid[level])))
        #print('\n')


def back_fill(array):
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

print(create_index(grid))
print(back_fill(grid))
create_grid(x, grid)


'''
create grid
choose random spot
create counter
while counter < total words
create temporary coords
    add letter
    if goes over the end
        break
    check if already filled
    if yes
        break
    else add to temp coords
    counter += 1
add word to grid using temp coords

'''

def choose_words():
    counter = 0
    while counter < number_of_words:
        for word in words:
            starting_point = (random.randint(0, x - 1), random.randint(0, y - 1))
            temp_coords = []
            word = [letter for letter in word]
            temp_coords.append([starting_point[0], starting_point[1]])
            break_point = 0
            for i in range(1, len(word)):
                try:
                    grid[starting_point[0], starting_point[1] + i] = word[i]
                    temp_coords.append([starting_point[0], starting_point[1] + i])
                except IndexError:
                    break_point = i
                    word = word[break_point:]
                    break
            if break_point > 0:
                for i in range(0, len(word)):
                    try:
                        grid[starting_point[0] + 1, [0 + i]] = word[i]
                        used_coords.append([starting_point[0] + 1, 0 + i])
                    except IndexError:
                        break