-- delete ods tables
drop table if exists ods_precipitations;
drop table if exists ods_temperatures;
drop table if exists ods_covid_features;

-- create ods tables
create table ods_precipitations (
    date date primary key,
    precipitation float,
    precipitation_normal float
);
create table ods_temperatures (
    date date primary key,
    min float,
    max float,
    normal_min float,
    normal_max float
);
create table ods_covid_features (
	 business_id varchar primary key,
	 delivery_or_takeout varchar,
	 grubhub_enabled varchar,
	 call_to_action_enabled varchar,
	 request_a_quote_enabled varchar,
	 temporary_closed_until varchar,
	 virtual_services_offered varchar
--	 covid_banner varchar, todo-explode
--	 highlights varchar,
);