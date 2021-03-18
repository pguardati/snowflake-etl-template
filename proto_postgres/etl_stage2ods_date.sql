insert into ods_checkins (
    business_id
)
select business_id
from checkins;

insert into ods_reviews (
	 review_id,
	 date,
	 business_id,
	 user_id,
	 stars,
	 useful,
	 funny,
	 cool,
	 text
)
select
	 review_id,
	 to_timestamp(date,'YYYY-MM-DD HH24:mi:ss') as date,
	 business_id,
	 user_id,
	 cast(stars as int),
	 cast(useful as int),
	 cast(funny as int),
	 cast(cool as int),
	 text
from reviews;

insert into ods_tips (
	 date,
	 user_id,
	 business_id,
	 compliment_count,
	 text
)
select
	to_timestamp(date,'YYYY-MM-DD HH24:mi:ss') as date,
    user_id,
    business_id,
    cast(compliment_count as int),
    text
from tips;

select * from ods_checkins;
select * from ods_tips;
select * from ods_reviews;
