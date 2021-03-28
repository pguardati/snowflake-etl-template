USE schema dwh;

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

