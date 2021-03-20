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
    cast(min AS float),
    cast(max AS float),
    cast(normal_min AS float),
    cast(normal_max AS float)
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