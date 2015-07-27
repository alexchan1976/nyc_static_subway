#!/usr/bin/env python
import csv
import ConfigParser




def read_stops(data_directory):
	full_path = data_directory+'/stops.txt'
	with open(full_path, 'rb') as csvfile:
		stops = csv.reader(csvfile, delimiter=',')
		for row in stops:
			sql ="INSERT INTO mta_stops ()"

app_config = ConfigParser.RawConfigParser()
app_config.read('mta_data.cfg');

read_dir = app_config.get('import','data_dir')

read_stops(read_dir)