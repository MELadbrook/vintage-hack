__author__ = 'MLadbrook'

import numpy as np
import random

words_four = {'help', 'dogs', 'cats', 'does'}
words_five = {'please', 'hello', 'tears', 'mouse'}

x = 10
y = 8
number_of_words = 2

punctuation = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')']

grid = np.full((x, y), ' ')

words = random.sample(words_five, number_of_words)
print(words)

