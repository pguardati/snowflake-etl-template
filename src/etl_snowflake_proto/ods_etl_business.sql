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
            staging.business
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
