USE schema staging;

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