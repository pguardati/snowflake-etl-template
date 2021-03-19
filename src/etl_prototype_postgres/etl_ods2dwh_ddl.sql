drop table if exists star_dim_weather cascade;
drop table if exists star_dim_business cascade;
drop table if exists star_dim_users cascade;
drop table if exists star_fact_reviews cascade;

create table star_dim_weather (
    weather_date timestamp primary key,
    precipitation float,
    precipitation_normal float,
    temperature_min float,
    temperature_max float,
    temperature_normal_min float,
    temperature_normal_max float
);

create table star_dim_business (
	 business_id varchar primary key,
	 business_name varchar,
	 business_city varchar,
	 business_stars float,
	 business_review_count int
);

create table star_dim_users (
	 user_id varchar primary key,
	 yelping_since timestamp,
	 user_name varchar,
	 user_average_stars float,
	 user_review_count int
);

create table star_fact_reviews (
	 review_id varchar primary key,
	 review_date timestamp references star_dim_weather(weather_date) ,
	 business_id varchar references star_dim_business(business_id),
	 user_id varchar references star_dim_users(user_id),
	 review_stars int,
	 review_text varchar
);