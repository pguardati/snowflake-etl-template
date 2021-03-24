USE DATABASE snowflake_db;

USE schema ods;

-- crate business ods
INSERT INTO
    business (
        -- process covid features
        WITH cf_processed AS (
            SELECT
                json_records :"business_id" AS business_id,
                CASE
                    WHEN json_records :"delivery or takeout" = 'FALSE' THEN false
                    ELSE TRUE
                END AS delivery_or_takeout,
                CASE
                    WHEN json_records :"Grubhub enabled" = 'FALSE' THEN false
                    ELSE TRUE
                END AS grubhub_enabled,
                CASE
                    WHEN json_records :"Call To Action enabled" = 'FALSE' THEN false
                    ELSE TRUE
                END AS call_to_action_enabled,
                CASE
                    WHEN json_records :"Request a Quote Enabled" = 'FALSE' THEN false
                    ELSE TRUE
                END AS request_a_quote_enabled,
                CASE
                    WHEN json_records :"Temporary Closed Until" = 'FALSE' THEN false
                    ELSE TRUE
                END AS temporary_closed_until,
                CASE
                    WHEN json_records :"Virtual Services Offered" = 'FALSE' THEN false
                    ELSE TRUE
                END AS virtual_services_offered
            FROM
                staging.covid_features
        ),
        -- process business features
        bf_processed AS (
            SELECT
                json_records :"business_id" AS business_id,
                json_records :"name" AS business_name,
                json_records :"address" AS business_address,
                json_records :"city" AS business_city,
                json_records :"state" AS business_state,
                json_records :"postal_code" AS business_postal_code,
                cast(json_records :"latitude" AS float) AS business_latitude,
                cast(json_records :"longitude" AS float) AS business_longitude,
                cast(json_records :"stars" AS float) AS business_stars,
                cast(json_records :"review_count" AS int) AS business_review_count,
                CASE
                    WHEN json_records :"is_open" = '0' THEN false
                    ELSE TRUE
                END AS business_is_open
            FROM
                staging.business_features
        ),
        -- process checkin features
        checkin_processed AS (
            SELECT
                json_records :business_id AS business_id,
                cast (json_records :date AS varchar) AS checkin_dates
            FROM
                staging.checkins
        )
        SELECT
            b.business_id,
            business_name,
            business_address,
            business_city,
            business_state,
            business_postal_code,
            business_latitude,
            business_longitude,
            business_stars,
            business_review_count,
            business_is_open,
            delivery_or_takeout,
            grubhub_enabled,
            call_to_action_enabled,
            request_a_quote_enabled,
            temporary_closed_until,
            virtual_services_offered,
            checkin_dates
        FROM
            bf_processed AS b
            JOIN cf_processed AS c ON b.business_id = c.business_id
            JOIN checkin_processed AS ck ON b.business_id = ck.business_id
    );

-- create weather ods
INSERT INTO
    weather (
        WITH t_processed AS (
            SELECT
                to_timestamp(date, 'YYYYMMDD') AS weather_date,
                cast(min AS float) AS temperature_min,
                cast(max AS float) AS temperature_max,
                cast(normal_min AS float) AS temperature_normal_min,
                cast(normal_max AS float) AS temperature_normal_max
            FROM
                staging.temperatures
        ),
        p_processed AS(
            SELECT
                to_timestamp(date, 'YYYYMMDD') AS weather_date,
                cast(precipitation AS float) AS precipitation,
                cast(precipitation_normal AS float) AS precipitation_normal
            FROM
                staging.precipitations
        )
        SELECT
            p.weather_date AS weather_date,
            p.precipitation,
            p.precipitation_normal,
            t.temperature_min,
            t.temperature_max,
            t.temperature_normal_min,
            t.temperature_normal_max
        FROM
            p_processed AS p
            JOIN t_processed AS t ON p.weather_date = t.weather_date
    );