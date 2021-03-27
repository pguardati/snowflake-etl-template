CREATE SCHEMA dwh;
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

-- fill tables from ods
INSERT INTO
	dim_weather
SELECT
	DISTINCT weather_date,
	precipitation,
	(temperature_min + temperature_max) / 2 AS temperature
FROM
	ods.weather;

INSERT INTO
	dim_business
SELECT
	DISTINCT business_id,
	business_name
FROM
	ods.business;

INSERT INTO
	fact_reviews WITH r AS (
		SELECT
			review_id,
			date_trunc('day', review_date) AS review_date,
			business_id,
			review_stars
		FROM
			ods.reviews
	)
SELECT
	DISTINCT r.*
FROM
	r
	JOIN dim_weather AS w ON r.review_date = w.weather_date
	JOIN dim_business AS b ON r.business_id = b.business_id;

-- business query
SELECT
	b.business_name,
    review_stars,
    w.temperature,
	w.precipitation
FROM
	fact_reviews AS r
	JOIN dim_weather AS w ON r.review_date = w.weather_date
	JOIN dim_business AS b ON r.business_id = b.business_id
ORDER BY
	business_name, review_stars, temperature;

