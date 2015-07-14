create table mta_agencies (
	agency_id varchar(255),
	agency_name varchar(255),
	agency_url varchar(255),
	agency_timezone varchar(255),
	agency_lang varchar(10),
	agency_phone varchar(12)
) ENGINE=InnoDB;

create table mta_stops (
	stop_id varchar(5),
	stop_code varchar(5),
	stop_name varchar(255),
	stop_desc varchar(255),
	stop_lat float,
	stop_lon float,
	zone_id varchar(255),
	stop_url varchar(255),
	location_type varchar(255),
	parent_station varchar(255)
) ENGINE=InnoDB;

create table mta_routes (
	route_id varchar(5),
	agency_id varchar(5),
	route_short_name varchar(255),
	route_long_name varchar(255),
	route_desc varchar(255),
	route_type varchar(255),
	route_url varchar(255),
	route_color varchar(255),
	route_text_color varchar(255)
) ENGINE=InnoDB;

create table mta_trips (
	route_id varchar(5),
	service_id varchar(255),
	trip_id varchar(255),
	trip_headsign varchar(255),
	direction_id varchar(255),
	block_id varchar(255),
	shape_id varchar(255)
) ENGINE=InnoDB;

create table mta_stop_times (
	trip_id varchar(5),
	arrival_time varchar(10),
	departure_time varchar(10),
	stop_id varchar(255),
	stop_sequence varchar(255),
	stop_headsign varchar(255),
	pickup_type varchar(255),
	drop_off_type varchar(255),
	shape_dist_traveled varchar(255)
)ENGINE=InnoDB;

create table mta_calendar (
	service_id varchar(255),
	monday tinyint,
	tuesday tinyint,
	wednesday tinyint,
	thursday tinyint,
	friday tinyint,
	saturday tinyint,
	sunday tinyint,
	start_date varchar(25),
	end_date varchar(25)
)ENGINE=InnoDB;

create table mta_calendar_dates (
	service_id varchar(255),
	`date` varchar(25),
	exception_type int
)ENGINE=InnoDB;

create table mta_shapes (
	shape_id varchar(20),
	shape_pt_lat float,
	shape_pt_lon float,
	shape_pt_sequence int,
	shape_dist_traveled varchar(255)
)ENGINE=InnoDB;

create table mta_transfers (
	from_stop_id varchar(5),
	to_stop_id varchar(5),
	transfer_type int,
	min_transfer_time int
)ENGINE=InnoDB;