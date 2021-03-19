-- fill dimension tables
insert into star_dim_weather
select
    p.weather_date,
    precipitation,
    precipitation_normal,
    min as temperature_min,
    max as temperature_max,
    normal_min as temperature_min,
    normal_max as temperature_max
from ods_precipitations as p
join ods_temperatures as t
on p.weather_date = t.weather_date;

insert into star_dim_business
select
	 business_id,
	 business_name,
	 city as business_city,
	 stars as business_stars,
	 review_count as business_review_count
from ods_business_features;

insert into star_dim_users
select
	 user_id,
	 yelping_since,
	 user_name,
	 average_stars as user_average_stars,
	 review_count as user_review_count
from ods_users;

-- fill fact table (use join to enforce data integrity)
insert into star_fact_reviews
with r as (
    select
        review_id,
        date_trunc('day',review_date) as review_date,
        business_id,
        user_id,
        stars as review_stars,
        review_text
    from ods_reviews
)
select r.* from r
join star_dim_weather as w
on r.review_date = w.weather_date
join star_dim_business as b
on r.business_id = b.business_id
join star_dim_users as u
on r.user_id = u.user_id
