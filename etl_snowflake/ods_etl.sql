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
                to_timestamp(date :: varchar, 'YYYYMMDD') AS weather_date,
                cast(min AS float) AS temperature_min,
                cast(max AS float) AS temperature_max,
                cast(normal_min AS float) AS temperature_normal_min,
                cast(normal_max AS float) AS temperature_normal_max
            FROM
                staging.temperatures
        ),
        p_processed AS(
            SELECT
                to_timestamp(date :: varchar, 'YYYYMMDD') AS weather_date,
                cast(precipitation AS float) AS precipitation,
                cast(precipitation_normal AS float) AS precipitation_normal
            FROM
                staging.precipitations
            WHERE
                is_real(precipitation) 
        )
        SELECT
            p.weather_date AS weather_date,
            t.temperature_min,
            t.temperature_max,
            t.temperature_normal_min,
            t.temperature_normal_max,
            p.precipitation,
            p.precipitation_normal
        FROM
            p_processed AS p
            JOIN t_processed AS t ON p.weather_date = t.weather_date
    );

-- create users ods
INSERT INTO
    users (
        SELECT
            json_records: user_id AS user_id,
            to_timestamp(json_records: yelping_since) AS user_yelping_since,
            json_records: "name" AS user_name,
            cast(json_records :average_stars AS float) AS user_average_stars,
            cast(json_records :review_count AS int) AS user_review_count,
            cast(json_records :useful AS int) AS useful,
            cast(json_records :funny AS int) AS funny,
            cast(json_records :cool AS int) AS cool,
            cast(json_records :fans AS int) AS fans,
            cast(json_records :compliment_hot AS int) AS compliment_hot,
            cast(json_records :compliment_more AS int) AS compliment_more,
            cast(json_records :compliment_profile AS int) AS compliment_profile,
            cast(json_records :compliment_cute AS int) AS compliment_cute,
            cast(json_records :compliment_list AS int) AS compliment_list,
            cast(json_records :compliment_note AS int) AS compliment_note,
            cast(json_records :compliment_plain AS int) AS compliment_plain,
            cast(json_records :compliment_cool AS int) AS compliment_cool,
            cast(json_records :compliment_funny AS int) AS compliment_funny,
            cast(json_records :compliment_writer AS int) AS compliment_writer,
            cast(json_records :compliment_photos AS int) AS compliment_photos
        FROM
            staging.users
    );

-- create tips ods
INSERT INTO
    tips (
        WITH processed_tips AS(
            SELECT
                to_timestamp(json_records :date) AS tips_date,
                json_records :user_id AS user_id,
                json_records :business_id AS business_id,
                cast(json_records :compliment_count AS int) AS compliment_count,
                json_records :text AS tips_text
            FROM
                staging.tips
        )
        SELECT
            t.tips_date,
            t.user_id,
            t.business_id,
            t.compliment_count,
            t.tips_text
        FROM
            processed_tips AS t
            JOIN business AS b ON t.business_id = b.business_id
            JOIN users AS u ON t.user_id = u.user_id
    );

-- create reviews ods
INSERT INTO
    reviews (
        WITH processed_reviews AS(
            SELECT
                json_records: review_id AS review_id,
                to_timestamp(json_records: date) AS review_date,
                date_trunc('day', to_date(review_date)) AS review_date_truncated,
                json_records: business_id AS business_id,
                json_records: user_id AS user_id,
                cast(json_records: stars AS int) AS review_stars,
                cast(json_records: useful AS int) AS useful,
                cast(json_records: funny AS int) AS funny,
                cast(json_records: cool AS int) AS cool,
                json_records: text AS review_text
            FROM
                staging.reviews
        )
        SELECT
            r.review_id,
            r.review_date,
            r.business_id,
            r.user_id,
            r.review_stars,
            r.useful,
            r.funny,
            r.cool,
            r.review_text
        FROM
            processed_reviews AS r
            JOIN business AS b ON r.business_id = b.business_id
            JOIN users AS u ON r.user_id = u.user_id
            JOIN weather AS w ON r.review_date_truncated = w.weather_date
    );