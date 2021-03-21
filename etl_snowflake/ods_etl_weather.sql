-- precipitations
INSERT INTO
    ods_precipitations
SELECT
    to_timestamp(date, 'YYYYMMDD') AS weather_date,
    cast(precipitation AS float),
    cast(precipitation_normal AS float)
FROM
    staging_precipitations AS p;

-- temperatures
INSERT INTO
    ods_temperatures
SELECT
    to_timestamp(date, 'YYYYMMDD') AS weather_date,
    cast(min AS float) AS temperature_min,
    cast(max AS float) AS temperature_max,
    cast(normal_min AS float) AS temperature_min,
    cast(normal_max AS float) AS temperature_max
FROM
    staging_temperatures AS p;

-- query results
SELECT
    *
FROM
    ods_temperatures;

SELECT
    *
FROM
    ods_precipitations;