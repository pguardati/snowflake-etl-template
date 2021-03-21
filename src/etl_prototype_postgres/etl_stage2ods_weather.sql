insert into ods_precipitations
select
    to_timestamp(date,'YYYYMMDD') as weather_date,
    cast(precipitation as float),
    cast(precipitation_normal as float)
from precipitations
as p
where (precipitation ~ '^[0-9\.]+$');


insert into ods_temperatures
select
    to_timestamp(date,'YYYYMMDD') as weather_date,
    cast(min as float),
    cast(max as float),
    cast(normal_min as float),
    cast(normal_max as float)
from temperatures
as p;

