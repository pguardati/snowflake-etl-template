USE DATABASE snowflake_db;

USE schema ods;

-- delete ods tables
DROP TABLE IF EXISTS weather CASCADE ;

DROP TABLE IF EXISTS business CASCADE;

DROP TABLE IF EXISTS users CASCADE;

DROP TABLE IF EXISTS tips CASCADE;

DROP TABLE IF EXISTS reviews CASCADE;


-- create ods tables
CREATE TABLE weather (
    weather_date timestamp,
    temperature_min float,
    temperature_max float,
    temperature_normal_min float,
    temperature_normal_max float,
    precipitation float,
    precipitation_normal float,
    CONSTRAINT pk_weather_id PRIMARY KEY (weather_date)
);

CREATE TABLE business(
    business_id varchar,
    business_name varchar,
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
    -- hours varchar,    
    delivery_or_takeout boolean,
    grubhub_enabled boolean,
    call_to_action_enabled boolean,
    request_a_quote_enabled boolean,
    temporary_closed_until boolean,
    virtual_services_offered boolean,
    -- covid_banner varchar
    -- highlights varcha
    checkin_dates varchar,
    CONSTRAINT pk_business_id PRIMARY KEY (business_id)
);

CREATE TABLE users (
    user_id varchar,
    user_yelping_since timestamp,
    user_name varchar,
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

CREATE TABLE tips (
    tips_id int IDENTITY(1,1),
    tips_date timestamp,
    user_id varchar,
    business_id varchar,
    compliment_count int,
    tips_text varchar,
    CONSTRAINT pk_tips_id PRIMARY KEY (tips_id),
    CONSTRAINT fk_business_id FOREIGN KEY (business_id) REFERENCES business(business_id),
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
    CONSTRAINT fk_date_id FOREIGN KEY (review_date) REFERENCES weather(weather_date),
    CONSTRAINT fk_business_id FOREIGN KEY (business_id) REFERENCES business(business_id),
    CONSTRAINT fk_user_id FOREIGN KEY (user_id) REFERENCES users(user_id)
);