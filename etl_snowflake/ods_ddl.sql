-- delete ods tables
DROP TABLE IF EXISTS precipitations;

DROP TABLE IF EXISTS temperatures;

DROP TABLE IF EXISTS covid_features;

DROP TABLE IF EXISTS business_features;

DROP TABLE IF EXISTS checkins;

DROP TABLE IF EXISTS reviews;

DROP TABLE IF EXISTS tips;

DROP TABLE IF EXISTS users;

-- create ods tables
CREATE TABLE precipitations (
	weather_date timestamp PRIMARY KEY,
	precipitation float,
	precipitation_normal float
);

CREATE TABLE temperatures (
	weather_date timestamp PRIMARY KEY,
	temperature_min float,
	temperature_max float,
	temperature_normal_min float,
	temperature_normal_max float
);

CREATE TABLE covid_features (
	business_id varchar PRIMARY KEY,
	delivery_or_takeout boolean,
	grubhub_enabled boolean,
	call_to_action_enabled boolean,
	request_a_quote_enabled boolean,
	temporary_closed_until boolean,
	virtual_services_offered boolean --	 covid_banner varchar,
	--	 highlights varchar,
);

CREATE TABLE business_features (
	business_id varchar PRIMARY KEY,
	business_name varchar,
	business_address varchar,
	business_city varchar,
	business_state varchar,
	business_postal_code varchar,
	business_latitude float,
	business_longitude float,
	business_stars float,
	business_review_count int,
	business_is_open boolean
	--	 attributes,
	--	 categories
	--	 hours
);

CREATE TABLE checkins (
	business_id varchar PRIMARY KEY --	 checkin_date timestamp 
);

CREATE TABLE tips (
	tips_date timestamp PRIMARY KEY,
	user_id varchar,
	business_id varchar,
	compliment_count int,
	tips_text varchar
);

CREATE TABLE reviews (
	review_id varchar PRIMARY KEY,
	review_date timestamp,
	business_id varchar,
	user_id varchar,
	review_stars int,
	useful int,
	funny int,
	cool int,
	review_text varchar
);

CREATE TABLE users (
	user_id varchar PRIMARY KEY,
	user_yelping_since timestamp,
	user_name varchar,
	user_average_stars float,
	user_review_count int,
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