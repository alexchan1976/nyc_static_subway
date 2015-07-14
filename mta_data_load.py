#!/usr/bin/env python
import csv

def read_stops():
	with open('stops.txt', 'rb') as csvfile:
		stops = csv.reader(csvfile, delimiter=',')
		for row in stops:
			print 


read_stops()