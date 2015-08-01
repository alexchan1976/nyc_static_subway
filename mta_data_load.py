#!/usr/bin/env python
import csv
import ConfigParser
import mta_models
from mta_models import *
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


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


#begin of agency import
print "begin agency import"
try:
	agency_file_name = read_dir + '/agency.txt'
	agency_list = Load_Data(agency_file_name)
	for i in agency_list:
		record = mta_agency()
		record.agency_id=i[0]
		record.agency_name=i[1]
		record.agency_url=i[2]
		record.agency_timezone=i[3]
		record.agency_lang=i[4]
		record.agency_phone=i[5]
		s.add(record) #Add all the records
		s.commit() #Attempt to commit all the records

except:
	print "agency import exception rollback called "
	#s.rollback() #Rollback the changes on error
finally:
	print "agency imported"
	#s.close() #Close the connection

#begin of STOPS import
print "begin stops import"
try:
	stops_file_name = read_dir + '/stops.txt'
	stops_list = Load_Data(stops_file_name)

	for i in stops_list:
		record = mta_stop()
		record.stop_id=i[0]
		record.stop_code=i[1]
		record.stop_name=i[2]
		record.stop_desc=i[3]
		record.stop_lat=i[4]
		record.stop_lon=i[5]
		record.zone_id=i[6]
		record.stop_url=i[7]
		record.location_type =i[8]
		record.parent_station = i[9]
		s.add(record) #Add all the records
		s.commit() #Attempt to commit all the records

except:
	print "stops import exception rollback called "
	#s.rollback() #Rollback the changes on error
finally:
	print "stops imported"
	#s.close() #Close the connection

