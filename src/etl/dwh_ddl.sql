USE schema dwh;

-- drop tables
DROP TABLE IF EXISTS dim_weather CASCADE;

DROP TABLE IF EXISTS dim_business CASCADE;

DROP TABLE IF EXISTS fact_reviews CASCADE;

-- create tables
CREATE TABLE dim_weather (
	weather_date timestamp,
	precipitation float,
	temperature float,
	CONSTRAINT pk_weather_id PRIMARY KEY (weather_date)
);

CREATE TABLE dim_business (
	business_id varchar,
	business_name varchar,
	CONSTRAINT pk_business_id PRIMARY KEY (business_id)
);

CREATE TABLE fact_reviews (
	review_id varchar,
	review_date timestamp,
	business_id varchar,
	review_stars int,
	CONSTRAINT pk_review_id PRIMARY KEY (review_id),
	CONSTRAINT fk_weather_id FOREIGN KEY (review_date) REFERENCES dim_weather(weather_date),
	CONSTRAINT fk_business_id FOREIGN KEY (business_id) REFERENCES dim_business(business_id)
);
