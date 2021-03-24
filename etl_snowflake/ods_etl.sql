USE DATABASE snowflake_db;

USE schema ods;

-- covid features
INSERT INTO
    covid_features WITH cf AS (
        SELECT
            json_records :"business_id" AS business_id,
            json_records :"delivery or takeout" AS delivery_or_takeout,
            json_records :"Grubhub enabled" AS grubhub_enabled,
            json_records :"Call To Action enabled" AS call_to_action_enabled,
            json_records :"Request a Quote Enabled" AS request_a_quote_enabled,
            json_records :"Temporary Closed Until" AS temporary_closed_until,
            json_records :"Virtual Services Offered" AS virtual_services_offered
        FROM
            staging.covid_features
    )
SELECT
    business_id,
    CASE
        WHEN delivery_or_takeout = 'FALSE' THEN false
        ELSE TRUE
    END AS delivery_or_takeout,
    CASE
        WHEN grubhub_enabled = 'FALSE' THEN false
        ELSE TRUE
    END AS grubhub_enabled,
    CASE
        WHEN call_to_action_enabled = 'FALSE' THEN false
        ELSE TRUE
    END AS call_to_action_enabled,
    CASE
        WHEN request_a_quote_enabled = 'FALSE' THEN false
        ELSE TRUE
    END AS request_a_quote_enabled,
    CASE
        WHEN temporary_closed_until = 'FALSE' THEN false
        ELSE TRUE
    END AS temporary_closed_until,
    CASE
        WHEN virtual_services_offered = 'FALSE' THEN false
        ELSE TRUE
    END AS virtual_services_offered
FROM
    cf;

--  business features
INSERT INTO
    business_features WITH bf AS (
        SELECT
            json_records :"business_id" AS business_id,
            json_records :"name" AS business_name,
            json_records :"address" AS business_address,
            json_records :"city" AS business_city,
            json_records :"state" AS business_state,
            json_records :"postal_code" AS business_postal_code,
            json_records :"latitude" AS business_latitude,
            json_records :"longitude" AS business_longitude,
            json_records :"stars" AS business_stars,
            json_records :"review_count" AS business_review_count,
            json_records :"is_open" AS business_is_open
        FROM
            staging.business_features
    )
SELECT
    business_id,
    business_name,
    business_address,
    business_city,
    business_state,
    business_postal_code,
    cast(business_latitude AS float),
    cast(business_longitude AS float),
    cast(business_stars AS float),
    cast(business_review_count AS int),
    CASE
        WHEN business_is_open = '0' THEN false
        ELSE TRUE
    END AS business_is_open
FROM
    bf;

-- checkins
INSERT INTO
    checkins (business_id)
SELECT
    json_records :business_id AS business_id
FROM
    staging.checkins;

-- users
INSERT INTO
    users WITH u AS (
        SELECT
            json_records: user_id AS user_id,
            json_records: yelping_since AS user_yelping_since,
            json_records: user_name AS user_name,
            json_records: average_stars AS user_average_stars,
            json_records: review_count AS user_review_count,
            json_records: useful AS useful,
            json_records: funny AS funny,
            json_records: cool AS cool,
            json_records: fans AS fans,
            json_records: compliment_hot AS compliment_hot,
            json_records: compliment_more AS compliment_more,
            json_records: compliment_profile AS compliment_profile,
            json_records: compliment_cute AS compliment_cute,
            json_records: compliment_list AS compliment_list,
            json_records: compliment_note AS compliment_note,
            json_records: compliment_plain AS compliment_plain,
            json_records: compliment_cool AS compliment_cool,
            json_records: compliment_funny AS compliment_funny,
            json_records: compliment_writer AS compliment_writer,
            json_records: compliment_photo AS compliment_photo
        FROM
            staging.users
    )
SELECT
    user_id,
    to_timestamp(user_yelping_since),
    user_name,
    cast(user_average_stars AS float),
    cast(user_review_count AS int),
    cast(useful AS int),
    cast(funny AS int),
    cast(cool AS int),
    cast(fans AS int),
    cast(compliment_hot AS int),
    cast(compliment_more AS int),
    cast(compliment_profile AS int),
    cast(compliment_cute AS int),
    cast(compliment_list AS int),
    cast(compliment_note AS int),
    cast(compliment_plain AS int),
    cast(compliment_cool AS int),
    cast(compliment_funny AS int),
    cast(compliment_writer AS int),
    cast(compliment_photo AS int)
FROM
    u;

-- precipitations
INSERT INTO
    precipitations
SELECT
    to_timestamp(date, 'YYYYMMDD') AS weather_date,
    cast(precipitation AS float),
    cast(precipitation_normal AS float)
FROM
    staging.precipitations AS p;

-- temperatures
INSERT INTO
    temperatures
SELECT
    to_timestamp(date, 'YYYYMMDD') AS weather_date,
    cast(min AS float) AS temperature_min,
    cast(max AS float) AS temperature_max,
    cast(normal_min AS float) AS temperature_min,
    cast(normal_max AS float) AS temperature_max
FROM
    staging.temperatures AS p;

-- tips
INSERT INTO
    tips WITH t AS (
        SELECT
            json_records :date AS date,
            json_records :user_id AS user_id,
            json_records :business_id AS business_id,
            json_records :compliment_count AS compliment_count,
            json_records :text AS text
        FROM
            staging.tips
    )
SELECT
    to_timestamp(date) AS date,
    user_id,
    business_id,
    cast(compliment_count AS int),
    text
FROM
    t;

-- reviews
INSERT INTO
    reviews WITH r AS (
        SELECT
            json_records: review_id AS review_id,
            json_records: date AS review_date,
            json_records: business_id AS business_id,
            json_records: user_id AS user_id,
            json_records: stars AS review_stars,
            json_records: useful AS useful,
            json_records: funny AS funny,
            json_records: cool AS cool,
            json_records: text AS review_text
        FROM
            staging.reviews
    )
SELECT
    review_id,
    to_timestamp(review_date),
    business_id,
    user_id,
    cast(review_stars AS int),
    cast(useful AS int),
    cast(funny AS int),
    cast(cool AS int),
    review_text
FROM
    r;