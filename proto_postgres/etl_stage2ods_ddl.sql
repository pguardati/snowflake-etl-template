-- delete ods tables
drop table if exists ods_precipitations;
drop table if exists ods_temperatures;

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
