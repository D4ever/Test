#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def countW(L):
	word = set(L)
	print (word)
	for a in word:
		x = L.count(a)
		print(a,': ',x)

f = open('test.txt','rb')
L=[]
content = f.read().decode()

L = content.split()

countW(L)
f.close()