#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import re, glob, shutil, datetime
#from datetime import datetime

name = glob.glob('output_*.txt')
datename = []
for a in name:
	if re.match('output_\d{1,4}.{1}\d{1,2}.{1}\d{1,2}.txt', a) != None:
		datename.append(a)

for b in datename:
	datenum = re.findall('\d{1,4}',b)
	t = datetime.datetime(int(datenum[0]),int(datenum[1]),int(datenum[2]))
	new1 = 'output_'+str(t.year)+'-'+str(t.month)+'-'+str(t.day)+'-'+str(t.weekday())+'.txt'
	if name.count(new1) == False:
		shutil.move(b, new1)