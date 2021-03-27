USE DATABASE snowflake_db;

USE schema staging;

-- create json staging files
CREATE
OR REPLACE FILE format json_records TYPE = 'JSON' strip_outer_array = TRUE;

CREATE
OR REPLACE stage file_json file_format = json_records;

-- create csv staging files
CREATE
OR REPLACE FILE format csv_records TYPE = csv FIELD_DELIMITER = ',' RECORD_DELIMITER = '\n' skip_header = 1 null_if = ('NULL', 'null') empty_field_as_null = TRUE compression = gzip error_on_column_count_mismatch = false;

CREATE
OR REPLACE stage file_csv file_format = csv_records;

-- drop staging tables
DROP TABLE IF EXISTS precipitations;

DROP TABLE IF EXISTS temperatures;

DROP TABLE IF EXISTS covid_features;

DROP TABLE IF EXISTS business_features;

DROP TABLE IF EXISTS checkins;

DROP TABLE IF EXISTS reviews;

DROP TABLE IF EXISTS tips;

DROP TABLE IF EXISTS users;

-- create staging tables
CREATE TABLE precipitations (
    date variant,
    precipitation variant,
    precipitation_normal variant
);

CREATE TABLE temperatures (
    date variant,
    min variant,
    max variant,
    normal_min variant,
    normal_max variant
);

CREATE TABLE IF NOT EXISTS covid_features (json_records variant);

CREATE TABLE IF NOT EXISTS business_features (json_records variant);

CREATE TABLE IF NOT EXISTS checkins (json_records variant);

CREATE TABLE IF NOT EXISTS reviews (json_records variant);

CREATE TABLE IF NOT EXISTS tips (json_records variant);

CREATE TABLE IF NOT EXISTS users (json_records variant);