-- delete ods tables
drop table if exists ods_precipitations;
drop table if exists ods_temperatures;
drop table if exists ods_covid_features;
drop table if exists ods_business_features;

-- create ods tables
create table ods_precipitations (
    date date primary key,
    precipitation float,
    precipitation_normal float
);
create table ods_temperatures (
    date date primary key,
    min float,
    max float,
    normal_min float,
    normal_max float
);
create table ods_covid_features (
	 business_id varchar primary key,
	 delivery_or_takeout bool,
	 grubhub_enabled bool,
	 call_to_action_enabled bool,
	 request_a_quote_enabled bool,
	 temporary_closed_until bool,
	 virtual_services_offered bool
--	 covid_banner varchar, todo-explode
--	 highlights varchar,
);
create table ods_business_features (
	 business_id varchar primary key,
	 "name" varchar,
	 address varchar,
	 city varchar,
	 state varchar,
	 postal_code varchar,
	 latitude float,
	 longitude float,
	 stars float,
	 review_count int,
	 is_open bool
--	 attributes, # todo: explode
--	 categories
--	 hours
);
