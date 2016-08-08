#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import random

n = input('Let\'s paly a game! Please enter a number:')
a = random.choice(range(0, int(n)))
ind = int(input('Now you can guess the number from 0 to what you enter: '))

while ind != a:
	if ind < a:
		ind = int(input('Your number is too small, please re-enter a number: '))
	else:
		ind = int(input('Your number is too large, please re-enter a number: '))

print('Congratulations! %d is the right number!' % ind)