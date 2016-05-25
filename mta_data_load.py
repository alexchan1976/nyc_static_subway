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
	s.rollback() #Rollback the changes on error
finally:
	print "agency finished imported"
	#s.close() #Close the connection

#begin of stops import
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
	s.rollback() #Rollback the changes on error
finally:
	print "stops finished imported"
	#s.close() #Close the connection

#begin of routes import
print "begin routes import"
try:
	routes_file_name = read_dir + '/routes.txt'
	routes_list = Load_Data(routes_file_name)
	for i in routes_list:
		record = mta_route()
		record.route_id=i[0]
		record.agency_id=i[1]
		record.route_short_name=i[2]
		record.route_long_name=i[3]
		record.route_desc=i[4]
		record.route_type=i[5]
		record.route_url=i[6]
		record.route_color=i[7]
		record.route_text_color=i[8]
		s.add(record) #Add all the records
		s.commit() #Attempt to commit all the records
except exc.SQLAlchemyError:
	print "routes import exception rollback called "
	print exc.SQLAlchemyError.message
	s.rollback() #Rollback the changes on error
finally:
	print "routes finish imported"
	s.close() #Close the connection


#begin of trips import
print "begin trips import"
try:
	trips_file_name = read_dir + '/trips.txt'
	trips_list = Load_Data(trips_file_name)
	for i in trips_list:
		record = mta_trip()
		record.route_id=i[0]
		record.service_id=i[1]
		record.trip_id=i[2]
		record.trip_headsign=i[3]
		record.direction_id=i[4]
		record.block_id=i[5]
		record.shape_id=i[6]
		s.add(record) #Add all the records
		s.commit() #Attempt to commit all the records
except exc.SQLAlchemyError:
	print "routes import exception rollback called "
	print exc.SQLAlchemyError.message
	s.rollback() #Rollback the changes on error
finally:
	print "routes finish imported"
	s.close() #Close the connection

#begin of stop times import
print "begin calendar import"
try:
	calendar_file_name = read_dir + '/calendar.txt'
	calendar_list = Load_Data(calendar_file_name)
	for i in calendar_list:
		record = mta_calendar()
		record.service_id=i[0]
		record.monday=i[1]
		record.tuesday=i[2]
		record.wednesday=i[3]
		record.thursday=i[4]
		record.friday=i[5]
		record.saturday=i[6]
		record.sunday=i[7]
		record.start_date=i[8]
		record.end_date=i[9]
		s.add(record) #Add all the records
		s.commit() #Attempt to commit all the records
except exc.SQLAlchemyError:
	print "stop times import exception rollback called "
	print exc.SQLAlchemyError.message
	s.rollback() #Rollback the changes on error
finally:
	print "stop times finish imported"
	s.close() #Close the connection



#begin of calendar date import
print "begin calendar date import"
try:
	calendar_date_file_name = read_dir + '/calendar_dates.txt'
	calendar_date_list = Load_Data(calendar_date_file_name)
	for i in calendar_date_list:
		record = mta_calendar_date()
		record.service_id=i[0]
		record.date=i[1]
		s.add(record) #Add all the records
		s.commit() #Attempt to commit all the records
except exc.SQLAlchemyError:
	print "calendar dates import exception rollback called "
	print exc.SQLAlchemyError.message
	s.rollback() #Rollback the changes on error
finally:
	print "calendar dates finish imported"

#begin of mta shap date import
print "begin mta_shape import"
try:
	shape_file_name = read_dir + '/shapes.txt'
	shape_list = Load_Data(shape_file_name)
	for i in shape_list:
		record = mta_shape()
		record.shape_id=i[0]
		record.shape_pt_lat=i[1]
		record.shape_pt_lon=i[2]
		record.shape_pt_sequence=i[3]
		s.add(record) #Add all the records
		s.commit() #Attempt to commit all the records
except exc.SQLAlchemyError:
	print "shapes import exception rollback called "
	print exc.SQLAlchemyError.message
	s.rollback() #Rollback the changes on error
finally:
	print "shapes finish imported"

#begin of mta shap date import
print "begin transfers import"
try:
	transfer_file_name = read_dir + '/transfers.txt'
	transfer_list = Load_Data(transfer_file_name)
	for i in transfer_list:
		record = mta_transfer()
		record.from_stop_id=i[0]
		record.to_stop_id=i[1]
		record.transfer_type=i[2]
		record.min_transfer_time=i[3]
		s.add(record) #Add all the records
		s.commit() #Attempt to commit all the records
except exc.SQLAlchemyError:
	print "transfers import exception rollback called "
	print exc.SQLAlchemyError.message
	s.rollback() #Rollback the changes on error
finally:
	print "transfers finish imported"