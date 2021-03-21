insert into ods_reviews
select
	 review_id,
	 to_timestamp(date,'YYYY-MM-DD HH24:mi:ss') as review_date,
	 business_id,
	 user_id,
	 cast(stars as int),
	 cast(useful as int),
	 cast(funny as int),
	 cast(cool as int),
	 text as review_text
from reviews;

insert into ods_users
select
	 user_id,
	 to_timestamp(yelping_since,'YYYY-MM-DD HH24:mi:ss') as yelping_since,
	 "name" as user_name,
	 cast(average_stars as float),
	 cast(review_count as int),
	 cast(useful as int),
	 cast(funny as int),
	 cast(cool as int),
	 cast(fans as int),
	 cast(compliment_hot as int),
	 cast(compliment_more as int),
	 cast(compliment_profile as int),
	 cast(compliment_cute as int),
	 cast(compliment_list as int),
	 cast(compliment_note as int),
	 cast(compliment_plain as int),
	 cast(compliment_cool as int),
	 cast(compliment_funny as int),
	 cast(compliment_writer as int),
	 cast(compliment_photos as int)
from users;
