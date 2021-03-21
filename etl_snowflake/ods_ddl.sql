-- delete ods tables
DROP TABLE IF EXISTS ods_precipitations;

DROP TABLE IF EXISTS ods_temperatures;

DROP TABLE IF EXISTS ods_covid_features;

DROP TABLE IF EXISTS ods_business_features;

DROP TABLE IF EXISTS ods_checkins;

DROP TABLE IF EXISTS ods_reviews;

DROP TABLE IF EXISTS ods_tips;

DROP TABLE IF EXISTS ods_users;

-- create ods tables
CREATE TABLE ods_precipitations (
	weather_date timestamp PRIMARY KEY,
	precipitation float,
	precipitation_normal float
);

CREATE TABLE ods_temperatures (
	weather_date timestamp PRIMARY KEY,
	temperature_min float,
	temperature_max float,
	temperature_normal_min float,
	temperature_normal_max float
);

CREATE TABLE ods_covid_features (
	business_id varchar PRIMARY KEY,
	delivery_or_takeout boolean,
	grubhub_enabled boolean,
	call_to_action_enabled boolean,
	request_a_quote_enabled boolean,
	temporary_closed_until boolean,
	virtual_services_offered boolean --	 covid_banner varchar,
	--	 highlights varchar,
);

CREATE TABLE ods_business_features (
	business_id varchar PRIMARY KEY,
	business_name varchar,
	address varchar,
	city varchar,
	state varchar,
	postal_code varchar,
	latitude float,
	longitude float,
	stars float,
	review_count int,
	is_open boolean --	 attributes,
	--	 categories
	--	 hours
);

CREATE TABLE ods_checkins (
	business_id varchar PRIMARY KEY --	 checkin_date timestamp 
);

CREATE TABLE ods_tips (
	tips_date timestamp PRIMARY KEY,
	user_id varchar,
	business_id varchar,
	compliment_count int,
	tips_text varchar
);

CREATE TABLE ods_reviews (
	review_id varchar PRIMARY KEY,
	review_date timestamp,
	business_id varchar,
	user_id varchar,
	stars int,
	useful int,
	funny int,
	cool int,
	review_text varchar
);

CREATE TABLE ods_users (
	user_id varchar PRIMARY KEY,
	yelping_since timestamp,
	user_name varchar,
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
	compliment_photos int --	 elite varchar,
	--	 friends varchar
);