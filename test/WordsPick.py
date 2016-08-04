#!/usr/bin/env python3
# -*- coding: utf-8 -*-

f = open('test.txt','rb')
L=[]
content = f.read().decode()

L = content.split()
word = set(L)
con = ''
for a in word:
    con = con + a + ' '

R = open('NewWord.txt,'w')

R.write(con)
R.close()
f.close()