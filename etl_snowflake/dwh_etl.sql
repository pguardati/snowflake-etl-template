-- fill dimension tables
INSERT INTO
    dim_weather
SELECT
    p.weather_date,
    precipitation,
    precipitation_normal,
	temperature_min,
	temperature_max,
	temperature_normal_min,
	temperature_normal_max
FROM
    ods.precipitations AS p
    JOIN ods.temperatures AS t ON p.weather_date = t.weather_date;


INSERT INTO
    dim_business
SELECT
    business_id,
    business_name,
    business_city,
    business_stars,
    business_review_count
FROM
    ods.business_features;

INSERT INTO
    dim_users
SELECT
    user_id,
    user_yelping_since,
    user_name,
    user_average_stars,
    user_review_count
FROM
    ods.users;

-- fill fact table (use join to enforce data integrity)
INSERT INTO
    fact_reviews WITH r AS (
        SELECT
            review_id,
            date_trunc('day', review_date) AS review_date,
            business_id,
            user_id,
            review_stars,
            review_text
        FROM
            ods.reviews
    )
SELECT
    r.*
FROM
    r
    JOIN star_dim_weather AS w ON r.review_date = w.weather_date
    JOIN star_dim_business AS b ON r.business_id = b.business_id
    JOIN star_dim_users AS u ON r.user_id = u.user_id;