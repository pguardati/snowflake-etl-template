--query to check if weather affects users' reviews
SELECT
    b.business_name,
    w.temperature_max,
    w.temperature_min,
    w.precipitation,
    review_stars,
    review_text
FROM
    star_fact_reviews AS r
    JOIN star_dim_weather AS w ON r.review_date = w.weather_date
    JOIN star_dim_business AS b ON r.business_id = b.business_id
    JOIN star_dim_users AS u ON r.user_id = u.user_id