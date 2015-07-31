#!/usr/bin/env python
import csv
import ConfigParser
import mta_models
from numpy import genfromtxt



def read_stops(r_dir):
	stop_file_name = r_dir + '/stops.txt'
	stops_list = Load_Data(stop_file_name)


def Load_Data(file_name):
    data = genfromtxt(file_name, delimiter=',', skiprows=1, converters={0: lambda s: str(s)})
    return data.tolist()

app_config = ConfigParser.RawConfigParser()
app_config.read('mta_data.cfg');

read_dir = app_config.get('import','data_dir')

read_stops(read_dir)