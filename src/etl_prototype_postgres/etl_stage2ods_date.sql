insert into ods_checkins (
    business_id
)
select business_id
from checkins;


insert into ods_tips (
	 tips_date,
	 user_id,
	 business_id,
	 compliment_count,
	 tips_text
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
