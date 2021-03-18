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

insert into ods_users (
	 user_id,
	 yelping_since,
	 "name",
	 average_stars,
	 review_count,
	 useful,
	 funny,
	 cool,
	 fans,
	 compliment_hot,
	 compliment_more,
	 compliment_profile,
	 compliment_cute,
	 compliment_list,
	 compliment_note,
	 compliment_plain,
	 compliment_cool,
	 compliment_funny,
	 compliment_writer,
	 compliment_photos
)
select
	 user_id,
	 to_timestamp(yelping_since,'YYYY-MM-DD HH24:mi:ss') as yelping_since,
	 "name",
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

select * from ods_reviews;
select * from ods_users;
