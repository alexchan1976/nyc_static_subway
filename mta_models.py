from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship
db = SQLAlchemy()

class mta_agency(db.Model):
	__tablename__ = "mta_agencies"
	id = db.Column(db.Integer, primary_key=True, nullable=False)
	agency_id = db.Column(db.String(255))
	agency_name = db.Column(db.String(255))
	agency_url =  db.Column(db.String(255))
	agency_timezone = db.Column(db.String(255))
	agency_lang = db.Column(db.String(10))
	agency_phone =  db.Column(db.String(12))


class mta_stop(db.Model):
	__tablename__ = "mta_stops"
	id = db.Column(db.Integer, primary_key=True, nullable=False)
	stop_id  = db.Column(db.String(5))
	stop_code = db.Column(db.String(5))
	stop_name = db.Column(db.String(255))
	stop_desc = db.Column(db.Text)
	stop_lat = db.Column(db.Float)
	stop_lon = db.Column(db.Float)
	zone_id = db.Column(db.String(255))
	stop_url = db.Column(db.String(255))
	location_type  = db.Column(db.String(255))
	parent_station  = db.Column(db.String(255))


class mta_route(db.Model):
	__tablename__ = "mta_routes"
	id = db.Column(db.Integer, primary_key=True, nullable=False)
	route_id  = db.Column(db.String(5))
	agency_id = db.Column(db.String(5))
	route_short_name = db.Column(db.String(255))
	route_long_name = db.Column(db.String(255))
	route_desc = db.Column(db.String(255))
	route_type = db.Column(db.String(255))
	route_url = db.Column(db.String(255))
	route_color = db.Column(db.String(255))
	route_text_color = db.Column(db.String(255))


class mta_trip(db.Model):
	__tablename__ = "mta_trips"
	id = db.Column(db.Integer, primary_key=True, nullable=False)
	route_id  = db.Column(db.String(5))
	service_id = db.Column(db.String(255))
	trip_id = db.Column(db.String(255))
	trip_headsign = db.Column(db.String(255))
	direction_id = db.Column(db.String(255))
	block_id  = db.Column(db.String(255))
	shape_id = db.Column(db.String(255))


class mta_stop_time(db.Model):
	__tablename__ = "mta_stop_times"
	id = db.Column(db.Integer, primary_key=True, nullable=False)
	trip_id = db.Column(db.String(5))
	arrival_time = db.Column(db.Time)
	departure_time =  db.Column(db.Time)
	stop_id  = db.Column(db.String(255))
	stop_sequence = db.Column(db.String(255))
	stop_headsign = db.Column(db.String(255))
	pickup_type = db.Column(db.String(255))
	drop_off_type = db.Column(db.String(255))
	shape_dist_traveled = db.Column(db.String(255))


class mta_calendar(db.Model):
	__tablename__ = "mta_calendar"
	id = db.Column(db.Integer, primary_key=True, nullable=False)
	service_id = db.Column(db.String(255))
	monday = db.Column(db.SmallInteger)
	tuesday = db.Column(db.SmallInteger)
	wednesday = db.Column(db.SmallInteger)
	thursday = db.Column(db.SmallInteger)
	friday = db.Column(db.SmallInteger)
	saturday = db.Column(db.SmallInteger)
	sunday = db.Column(db.SmallInteger)
	start_date = db.Column(db.String(25))
	end_date = db.Column(db.String(25))


class mta_calendar_date(db.Model):
	__tablename__ = "mta_calendar_dates"
	id = db.Column(db.Integer, primary_key=True, nullable=False)
	service_id = db.Column(db.String(255))
	date = db.Column(db.String(25))
	exception_type = db.Column(db.Integer)


class mta_shape(db.Model):
	__tablename__ = "mta_shapes"
	id = db.Column(db.Integer, primary_key=True, nullable=False)
	shape_id = db.Column(db.String(20))
	shape_pt_lat = db.Column(db.Float)
	shape_pt_lon = db.Column(db.Float)
	shape_pt_sequence = db.Column(db.Integer)
	shape_dist_traveled = db.Column(db.String(255))


class mta_transfer(db.Model):
	__tablename__ = "mta_transfers"
	id = db.Column(db.Integer, primary_key=True, nullable=False)
	from_stop_id = db.Column(db.String(5))
	to_stop_id = db.Column(db.String(5))
	transfer_type = db.Column(db.Integer)
	min_transfer_time = db.Column(db.Integer)
