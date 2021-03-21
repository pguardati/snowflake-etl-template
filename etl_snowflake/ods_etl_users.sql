USE DATABASE snowflake_db;

USE SCHEMA public;

INSERT INTO
    ods_reviews WITH r AS (
        SELECT
            json_records: review_id AS review_id,
            json_records: date AS date,
            json_records: business_id AS business_id,
            json_records: user_id AS user_id,
            json_records: stars AS stars,
            json_records: useful AS useful,
            json_records: funny AS funny,
            json_records: cool AS cool,
            json_records: text AS text
        FROM
            staging_reviews
    )
SELECT
    review_id,
    to_timestamp(date) AS review_date,
    business_id,
    user_id,
    cast(stars AS int),
    cast(useful AS int),
    cast(funny AS int),
    cast(cool AS int),
    text AS review_text
FROM
    r;

INSERT INTO
    ods_users WITH u AS (
        SELECT
            json_records: user_id AS user_id,
            json_records: yelping_since AS yelping_since,
            json_records: user_name AS user_name,
            json_records: average_stars AS average_stars,
            json_records: review_count AS review_count,
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
            staging_users
    )
SELECT
    user_id,
    to_timestamp(yelping_since) AS yelping_since,
    user_name,
    cast(average_stars AS float),
    cast(review_count AS int),
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