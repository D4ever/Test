#! /usr/bin/env python3
# -*- coding: utf-8 -*-

def wordrm(s):
	a = ''
	index = []
	sr = tuple(s.split())
	for i in sr:
		if i in index:
			pass
		else:
			a = a + str(i) + ' '
			index.append(i)
	return a

f = open('test.txt')
st = f.read()
f1 = open('measure.txt','w')
f1.write(wordrm(st))
f.close()
f1.close()