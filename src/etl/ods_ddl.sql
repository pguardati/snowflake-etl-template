USE schema ods;

-- delete ods tables
DROP TABLE IF EXISTS temperatures CASCADE;

DROP TABLE IF EXISTS precipitations CASCADE;

DROP TABLE IF EXISTS business_features CASCADE;

DROP TABLE IF EXISTS covid_features CASCADE;

DROP TABLE IF EXISTS checkins CASCADE;

DROP TABLE IF EXISTS users CASCADE;

DROP TABLE IF EXISTS tips CASCADE;

DROP TABLE IF EXISTS reviews CASCADE;

-- weather tables
CREATE TABLE temperatures (
    weather_date timestamp,
    temperature_min float NOT NULL,
    temperature_max float NOT NULL,
    temperature_normal_min float,
    temperature_normal_max float,
    CONSTRAINT pk_weather_id PRIMARY KEY (weather_date)
);

CREATE TABLE precipitations (
    weather_date timestamp,
    precipitation float NOT NULL,
    precipitation_normal float NOT NULL
);

-- business tables
CREATE TABLE business_features(
    business_id varchar,
    business_name varchar NOT NULL,
    business_address varchar,
    business_city varchar,
    business_state varchar,
    business_postal_code varchar,
    business_latitude float,
    business_longitude float,
    business_stars float,
    business_review_count int,
    business_is_open boolean,
    -- attributes varchar,
    -- categories varchar,
    -- hours varchar
    CONSTRAINT pk_business_id PRIMARY KEY (business_id)
);

CREATE TABLE covid_features(
    business_id varchar,
    delivery_or_takeout boolean,
    grubhub_enabled boolean,
    call_to_action_enabled boolean,
    request_a_quote_enabled boolean,
    temporary_closed_until boolean,
    virtual_services_offered boolean -- covid_banner varchar,
    -- highlights varchar,
);

CREATE TABLE checkins (
    business_id varchar,
    checkin_dates varchar
);

-- user tables
CREATE TABLE users (
    user_id varchar,
    user_yelping_since timestamp NOT NULL,
    user_name varchar NOT NULL,
    user_average_stars float,
    user_review_count int,
    useful int,
    funny int,
    cool int,
    fans int,
    compliment_hot int,
    compliment_more int,
    compliment_profile int,
    compliment_cute int,
    compliment_list int,
    compliment_note int,
    compliment_plain int,
    compliment_cool int,
    compliment_funny int,
    compliment_writer int,
    compliment_photos int,
    -- elite varchar,
    -- friends varchar,
    CONSTRAINT pk_business_id PRIMARY KEY (user_id)
);

-- transaction tables
CREATE TABLE tips (
    tips_date timestamp,
    user_id varchar,
    business_id varchar,
    compliment_count int,
    tips_text varchar,
    CONSTRAINT pk_tips_id PRIMARY KEY (tips_date),
    CONSTRAINT fk_business_id FOREIGN KEY (business_id) REFERENCES business_features(business_id),
    CONSTRAINT fk_user_id FOREIGN KEY (user_id) REFERENCES users(user_id)
);

CREATE TABLE reviews (
    review_id varchar,
    review_date timestamp,
    business_id varchar,
    user_id varchar,
    review_stars int,
    useful int,
    funny int,
    cool int,
    review_text varchar,
    CONSTRAINT pk_review_id PRIMARY KEY (review_id),
    CONSTRAINT fk_date_id FOREIGN KEY (review_date) REFERENCES temperatures(weather_date),
    CONSTRAINT fk_business_id FOREIGN KEY (business_id) REFERENCES business_features(business_id),
    CONSTRAINT fk_user_id FOREIGN KEY (user_id) REFERENCES users(user_id)
);