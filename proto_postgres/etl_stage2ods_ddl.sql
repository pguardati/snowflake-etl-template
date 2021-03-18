-- delete ods tables
drop table if exists ods_precipitations;
drop table if exists ods_temperatures;
drop table if exists ods_covid_features;
drop table if exists ods_business_features;
drop table if exists ods_checkins;
drop table if exists ods_reviews;
drop table if exists ods_tips;
drop table if exists ods_users;

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

create table ods_checkins (
	 business_id varchar primary key
--	 date timestamp todo: explode
);

create table ods_tips (
	 date timestamp primary key,
	 user_id varchar,
	 business_id varchar,
	 compliment_count int,
	 text varchar
);

create table ods_reviews (
	 review_id varchar primary key,
	 date timestamp,
	 business_id varchar,
	 user_id varchar,
	 stars int,
	 useful int,
	 funny int,
	 cool int,
	 text varchar
);

create table ods_users (
	 user_id varchar,
	 yelping_since timestamp,
	 "name" varchar,
	 average_stars float,
	 review_count int,
	 useful int,
	 funny int,
	 cool int,
	 fans int,
	 compliment_hot int,
	 compliment_more int,
	 compliment_profile int,
	 compliment_cute int,
	 compliment_list int,
	 compliment_note int,
	 compliment_plain int,
	 compliment_cool int,
	 compliment_funny int,
	 compliment_writer int,
	 compliment_photos int
--	 elite varchar,
--	 friends varchar,
);
