USE schema dwh;

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
	business_name,
	review_stars,
	temperature;