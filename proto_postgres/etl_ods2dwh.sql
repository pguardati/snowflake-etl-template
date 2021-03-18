--merge weather data
insert into star_dim_weather
select
    p.weather_date,
    precipitation,
    precipitation_normal,
    min,
    max,
    normal_min,
    normal_max
from ods_precipitations as p
join ods_temperatures as t
on p.weather_date = t.weather_date

--delete review_date seconds in reviews

--