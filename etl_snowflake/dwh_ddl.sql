DROP TABLE IF EXISTS dim_weather CASCADE;

DROP TABLE IF EXISTS dim_business CASCADE;

DROP TABLE IF EXISTS dim_users CASCADE;

DROP TABLE IF EXISTS fact_reviews CASCADE;

CREATE TABLE dim_weather (
	weather_date timestamp PRIMARY KEY,
	precipitation float,
	precipitation_normal float,
	temperature_min float,
	temperature_max float,
	temperature_normal_min float,
	temperature_normal_max float
);

CREATE TABLE dim_business (
	business_id varchar PRIMARY KEY,
	business_name varchar,
	business_city varchar,
	business_stars float,
	business_review_count int
);

CREATE TABLE dim_users (
	user_id varchar PRIMARY KEY,
	yelping_since timestamp,
	user_name varchar,
	user_average_stars float,
	user_review_count int
);

CREATE TABLE fact_reviews (
	review_id varchar PRIMARY KEY,
	review_date timestamp REFERENCES star_dim_weather(weather_date),
	business_id varchar REFERENCES star_dim_business(business_id),
	user_id varchar REFERENCES star_dim_users(user_id),
	review_stars int,
	review_text varchar
);