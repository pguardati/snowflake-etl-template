insert into ods_precipitations (
   date,
   precipitation,
   precipitation_normal
)
select
    to_date(date,'YYYYMMDD') as date,
    cast(precipitation as float),
    cast(precipitation_normal as float)
from precipitations
as p;

insert into ods_temperatures (
   date,
   min,
   max,
   normal_min,
   normal_max
)
select
    to_date(date,'YYYYMMDD') as date,
    cast(min as float),
    cast(max as float),
    cast(normal_min as float),
    cast(normal_max as float)
from temperatures
as p;

select * from ods_temperatures;
select * from ods_precipitations;
