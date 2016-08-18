#! /usr/bin/env python3
# -*- coding: utf-8 -*-

def wordcounts(s):
	dic = {}
	sr = s.split()
	word = set(sr)
	for i in word:
		dic[i] = sr.count(i)

	print (dic)

f = open('test.txt')
st = f.read()
wordcounts(st)

f.close()