#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def pri(n):
	global index
	index = 0
	if n == 1:
		print ('No prime number')
	else:
		print(2)
		for i in range(2,n):
			for j in range(2,i):
				if i%j == 0:
					index = j
					break
				index = j
			if index == i-1:
				print(i)


n = int(input('Please enter a positive integer: '))

if n <= 0:
	print('Please check your enter.')
else:
	pri(n)