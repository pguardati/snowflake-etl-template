-- checkins
INSERT INTO
    checkins (business_id)
SELECT
    json_records :business_id AS business_id
FROM
    staging.checkins;

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
