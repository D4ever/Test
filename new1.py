#! /usr/bin/env python3
# -*- coding: utf-8 -*-

class animals:
	def bark(self):
		print ('animals can bark')

class dog(animals):
	def bark(self):
		print('wangwang')

class cat(animals):
	def bark(self):
		print('miaomiao')

bird = animals()
husky = dog()
caffy = cat()
bird.bark()
husky.bark()
caffy.bark()