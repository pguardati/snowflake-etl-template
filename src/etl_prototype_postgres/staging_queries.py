"""FULL QUERIES"""

cmd_query_tables="""
select * from precipitations;
select * from temperatures;
select * from covid_features;
select * from business;
select * from checkins;
select * from reviews;
select * from tips;
select * from users;
"""

"""DELETE QUERIES"""
cmd_delete_tables="""
drop table if exists precipitations;
drop table if exists temperatures;
drop table if exists covid_features;
drop table if exists business;
drop table if exists checkins;
drop table if exists reviews;
drop table if exists tips;
drop table if exists users;
"""

"""CREATE QUERIES"""

cmd_create_tables="""
create table precipitations (
	 "date" varchar,
	 "precipitation" varchar,
	 "precipitation_normal" varchar
);
create table temperatures (
	 "date" varchar,
	 "min" varchar,
	 "max" varchar,
	 "normal_min" varchar,
	 "normal_max" varchar
);
create table covid_features (
	 "business_id" varchar,
	 "highlights" varchar,
	 "delivery or takeout" varchar,
	 "Grubhub enabled" varchar,
	 "Call To Action enabled" varchar,
	 "Request a Quote Enabled" varchar,
	 "Covid Banner" varchar,
	 "Temporary Closed Until" varchar,
	 "Virtual Services Offered" varchar
);
create table business (
	 "business_id" varchar,
	 "name" varchar,
	 "address" varchar,
	 "city" varchar,
	 "state" varchar,
	 "postal_code" varchar,
	 "latitude" varchar,
	 "longitude" varchar,
	 "stars" varchar,
	 "review_count" varchar,
	 "is_open" varchar,
	 "attributes" varchar,
	 "categories" varchar,
	 "hours" varchar
);
create table checkins (
	 "business_id" varchar,
	 "date" varchar
);
create table reviews (
	 "review_id" varchar,
	 "user_id" varchar,
	 "business_id" varchar,
	 "stars" varchar,
	 "useful" varchar,
	 "funny" varchar,
	 "cool" varchar,
	 "text" varchar,
	 "date" varchar
);
create table tips (
	 "user_id" varchar,
	 "business_id" varchar,
	 "text" varchar,
	 "date" varchar,
	 "compliment_count" varchar
);
create table users (
	 "user_id" varchar,
	 "name" varchar,
	 "review_count" varchar,
	 "yelping_since" varchar,
	 "useful" varchar,
	 "funny" varchar,
	 "cool" varchar,
	 "elite" varchar,
	 "friends" varchar,
	 "fans" varchar,
	 "average_stars" varchar,
	 "compliment_hot" varchar,
	 "compliment_more" varchar,
	 "compliment_profile" varchar,
	 "compliment_cute" varchar,
	 "compliment_list" varchar,
	 "compliment_note" varchar,
	 "compliment_plain" varchar,
	 "compliment_cool" varchar,
	 "compliment_funny" varchar,
	 "compliment_writer" varchar,
	 "compliment_photos" varchar
);
"""

"""INSERT QUERIES"""

cmd_insert_precipitations="""
insert into precipitations (
	 "date",
	 "precipitation",
	 "precipitation_normal"
)
values (%s, %s, %s); 
"""

cmd_insert_temperatures="""
insert into temperatures (
	 "date",
	 "min",
	 "max",
	 "normal_min",
	 "normal_max"
)
values (%s, %s, %s, %s, %s); 
"""

cmd_insert_covid_features="""
insert into covid_features (
	 "business_id",
	 "highlights",
	 "delivery or takeout",
	 "Grubhub enabled",
	 "Call To Action enabled",
	 "Request a Quote Enabled",
	 "Covid Banner",
	 "Temporary Closed Until",
	 "Virtual Services Offered"
)
values (%s, %s, %s, %s, %s, %s, %s, %s, %s); 
"""

cmd_insert_business="""
insert into business (
	 "business_id",
	 "name",
	 "address",
	 "city",
	 "state",
	 "postal_code",
	 "latitude",
	 "longitude",
	 "stars",
	 "review_count",
	 "is_open",
	 "attributes",
	 "categories",
	 "hours"
)
values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s); 
"""

cmd_insert_checkins="""
insert into checkins (
	 "business_id",
	 "date"
)
values (%s, %s); 
"""

cmd_insert_reviews="""
insert into reviews (
	 "review_id",
	 "user_id",
	 "business_id",
	 "stars",
	 "useful",
	 "funny",
	 "cool",
	 "text",
	 "date"
)
values (%s, %s, %s, %s, %s, %s, %s, %s, %s); 
"""

cmd_insert_tips="""
insert into tips (
	 "user_id",
	 "business_id",
	 "text",
	 "date",
	 "compliment_count"
)
values (%s, %s, %s, %s, %s); 
"""

cmd_insert_users="""
insert into users (
	 "user_id",
	 "name",
	 "review_count",
	 "yelping_since",
	 "useful",
	 "funny",
	 "cool",
	 "elite",
	 "friends",
	 "fans",
	 "average_stars",
	 "compliment_hot",
	 "compliment_more",
	 "compliment_profile",
	 "compliment_cute",
	 "compliment_list",
	 "compliment_note",
	 "compliment_plain",
	 "compliment_cool",
	 "compliment_funny",
	 "compliment_writer",
	 "compliment_photos"
)
values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s); 
"""


