#! /usr/bin/env python3
# -*- coding: utf-8 -*-

def prime(n):
	x = []
	if n <= 0:
		print('no prime')
	else:
		for i in range(2,n+1):
			for j in range(2,i+1):
				if i % j ==0:
					break
			if i ==j:
				x.append(int(i))
	print(x)
n = int(input('Please input a number(n), we will give you all prime in 0 ~ n: '))
prime(n)