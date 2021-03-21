-- fill dimension tables
INSERT INTO
    star_dim_weather
SELECT
    p.weather_date,
    precipitation,
    precipitation_normal,
    min AS temperature_min,
    max AS temperature_max,
    normal_min AS temperature_min,
    normal_max AS temperature_max
FROM
    ods_precipitations AS p
    JOIN ods_temperatures AS t ON p.weather_date = t.weather_date;

INSERT INTO
    star_dim_business
SELECT
    business_id,
    business_name,
    city AS business_city,
    stars AS business_stars,
    review_count AS business_review_count
FROM
    ods_business_features;

INSERT INTO
    star_dim_users
SELECT
    user_id,
    yelping_since,
    user_name,
    average_stars AS user_average_stars,
    review_count AS user_review_count
FROM
    ods_users;

-- fill fact table (use join to enforce data integrity)
INSERT INTO
    star_fact_reviews WITH r AS (
        SELECT
            review_id,
            date_trunc('day', review_date) AS review_date,
            business_id,
            user_id,
            stars AS review_stars,
            review_text
        FROM
            ods_reviews
    )
SELECT
    r.*
FROM
    r
    JOIN star_dim_weather AS w ON r.review_date = w.weather_date
    JOIN star_dim_business AS b ON r.business_id = b.business_id
    JOIN star_dim_users AS u ON r.user_id = u.user_id