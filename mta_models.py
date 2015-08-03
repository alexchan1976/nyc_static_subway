from sqlalchemy import *
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class mta_agency(Base):
	__tablename__ = "mta_agencies"
	id = Column(Integer, primary_key=True, nullable=False)
	agency_id = Column(String(255))
	agency_name = Column(String(255))
	agency_url =  Column(String(255))
	agency_timezone = Column(String(255))
	agency_lang = Column(String(10))
	agency_phone =  Column(String(12))


class mta_stop(Base):
	__tablename__ = "mta_stops"
	id = Column(Integer, primary_key=True, nullable=False)
	stop_id  = Column(String(5))
	stop_code = Column(String(5))
	stop_name = Column(String(255))
	stop_desc = Column(Text)
	stop_lat = Column(Float)
	stop_lon = Column(Float)
	zone_id = Column(String(255))
	stop_url = Column(String(255))
	location_type  = Column(String(255))
	parent_station  = Column(String(255))


class mta_route(Base):
	__tablename__ = "mta_routes"
	id = Column(Integer, primary_key=True, nullable=False)
	route_id  = Column(String(5))
	agency_id = Column(String(5))
	route_short_name = Column(String(255))
	route_long_name = Column(String(255))
	route_desc = Column(String(255))
	route_type = Column(String(255))
	route_url = Column(String(255))
	route_color = Column(String(255))
	route_text_color = Column(String(255))


class mta_trip(Base):
	__tablename__ = "mta_trips"
	id = Column(Integer, primary_key=True, nullable=False)
	route_id  = Column(String(5))
	service_id = Column(String(255))
	trip_id = Column(String(255))
	trip_headsign = Column(String(255))
	direction_id = Column(String(255))
	block_id  = Column(String(255))
	shape_id = Column(String(255))


class mta_stop_time(Base):
	__tablename__ = "mta_stop_times"
	id = Column(Integer, primary_key=True, nullable=False)
	trip_id = Column(String(5))
	arrival_time = Column(Time)
	departure_time =  Column(Time)
	stop_id  = Column(String(255))
	stop_sequence = Column(String(255))
	stop_headsign = Column(String(255))
	pickup_type = Column(String(255))
	drop_off_type = Column(String(255))
	shape_dist_traveled = Column(String(255))


class mta_calendar(Base):
	__tablename__ = "mta_calendar"
	id = Column(Integer, primary_key=True, nullable=False)
	service_id = Column(String(255))
	monday = Column(SmallInteger)
	tuesday = Column(SmallInteger)
	wednesday = Column(SmallInteger)
	thursday = Column(SmallInteger)
	friday = Column(SmallInteger)
	saturday = Column(SmallInteger)
	sunday = Column(SmallInteger)
	start_date = Column(String(25))
	end_date = Column(String(25))


class mta_calendar_date(Base):
	__tablename__ = "mta_calendar_dates"
	id = Column(Integer, primary_key=True, nullable=False)
	service_id = Column(String(255))
	date = Column(String(25))
	exception_type = Column(Integer)


class mta_shape(Base):
	__tablename__ = "mta_shapes"
	id = Column(Integer, primary_key=True, nullable=False)
	shape_id = Column(String(20))
	shape_pt_lat = Column(Float)
	shape_pt_lon = Column(Float)
	shape_pt_sequence = Column(Integer)
	shape_dist_traveled = Column(String(255))


class mta_transfer(Base):
	__tablename__ = "mta_transfers"
	id = Column(Integer, primary_key=True, nullable=False)
	from_stop_id = Column(String(5))
	to_stop_id = Column(String(5))
	transfer_type = Column(Integer)
	min_transfer_time = Column(Integer)
