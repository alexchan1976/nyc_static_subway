#!/usr/bin/env python
import csv
import ConfigParser
import mta_models
from mta_models import *
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import exc

#small function load file
def Load_Data(file_name):
	formatted = []
	with open(file_name, 'rb') as csvfile:
		rows = csv.reader(csvfile, delimiter=',')
		next(rows, None) 
		for row in rows:
			formatted.append(row)
		return formatted


#this where configuration is initialized 
app_config = ConfigParser.RawConfigParser()
app_config.read('mta_data.cfg')
read_dir = app_config.get('import','data_dir')
database_url = app_config.get('data','engine_url')

#SQLAlchemy initialization 
Base = declarative_base()
engine = create_engine(database_url)
Base.metadata.create_all(engine)

#set up data base session
   #Create the session
session = sessionmaker()
session.configure(bind=engine)
s = session()

#begin of stop times import
print "begin stop times import"
try:
	stop_times_file_name = read_dir + '/stop_times.txt'
	stop_times_list = Load_Data(stop_times_file_name)
	for i in stop_times_list:
		record = mta_stop_time()
		record.trip_id=i[0]
		record.arrival_time=i[1]
		record.departure_time=i[2]
		record.stop_id=i[3]
		record.stop_sequence=i[4]
		record.stop_headsign=i[5]
		record.pickup_type=i[6]
		record.drop_off_type=i[7]
		record.shape_dist_traveled=i[8]
		s.add(record) #Add all the records
		s.commit() #Attempt to commit all the records
except exc.SQLAlchemyError:
	print "stop times import exception rollback called "
	print exc.SQLAlchemyError.message
	s.rollback() #Rollback the changes on error
finally:
	print "stop times finish imported"
	s.close() #Close the connectio