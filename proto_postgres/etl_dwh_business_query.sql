select
    review_id,
    review_stars,
    review_text,
    w.*,
    b.*,
    u.*
from star_fact_reviews as r
join star_dim_weather as w
on r.review_date = w.weather_date
join star_dim_business as b
on r.business_id = b.business_id
join star_dim_users as u
on r.user_id = u.user_id
