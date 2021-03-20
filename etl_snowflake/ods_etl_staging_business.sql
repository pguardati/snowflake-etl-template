INSERT INTO
    ods_covid_features WITH cf AS (
        SELECT
            json_records :"business_id" as business_id,
            json_records :"delivery or takeout" AS delivery_or_takeout,
            json_records :"Grubhub enabled" AS grubhub_enabled,
            json_records :"Call To Action enabled" AS call_to_action_enabled,
            json_records :"Request a Quote Enabled" AS request_a_quote_enabled,
            json_records :"Temporary Closed Until" AS temporary_closed_until,
            json_records :"Virtual Services Offered" AS virtual_services_offered
        FROM
            covid_features
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


INSERT INTO
    ods_business_features WITH bf AS (
        SELECT
            json_records :"business_id" as business_id,
            json_records :"name" as name,
            json_records :"business_name" AS business_name,
            json_records :"address" AS address,
            json_records :"city" AS city,
            json_records :"state" AS state,
            json_records :"postal_code" AS postal_code,
            json_records :"latitude" AS latitude,
            json_records :"longitude" AS longitude,
            json_records :"stars" AS stars,
            json_records :"review_count" AS review_count,
            json_records :"is_open" AS is_open 
        FROM
            business
    )
SELECT
    business_id,
    name AS business_name,
    address,
    city,
    state,
    postal_code,
    cast(latitude AS float),
    cast(longitude AS float),
    cast(stars AS float),
    cast(review_count AS int),
    CASE
        WHEN is_open = '0' THEN false
        ELSE TRUE
    END AS is_open
FROM
    bf;

SELECT
    *
FROM
    ods_covid_features;

SELECT
    *
FROM
    ods_business_features;