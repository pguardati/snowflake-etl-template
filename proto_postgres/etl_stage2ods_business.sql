insert into ods_covid_features (
	 business_id,
	 delivery_or_takeout,
	 grubhub_enabled,
	 call_to_action_enabled,
	 request_a_quote_enabled,
	 temporary_closed_until,
	 virtual_services_offered
	)
with cf as (
    select
         "business_id",
         "delivery or takeout" as delivery_or_takeout,
         "Grubhub enabled" as grubhub_enabled,
         "Call To Action enabled" as call_to_action_enabled,
         "Request a Quote Enabled" as request_a_quote_enabled,
         "Temporary Closed Until" as temporary_closed_until,
         "Virtual Services Offered" as virtual_services_offered
    from covid_features
)
select
    business_id,
    CASE WHEN delivery_or_takeout = 'FALSE' THEN false ELSE true END as delivery_or_takeout,
    CASE WHEN grubhub_enabled = 'FALSE' THEN false ELSE true END as grubhub_enabled,
    CASE WHEN call_to_action_enabled = 'FALSE' THEN false ELSE true END as call_to_action_enabled,
    CASE WHEN request_a_quote_enabled = 'FALSE' THEN false ELSE true END as request_a_quote_enabled,
    CASE WHEN temporary_closed_until = 'FALSE' THEN false ELSE true END as temporary_closed_until,
    CASE WHEN virtual_services_offered = 'FALSE' THEN false ELSE true END as virtual_services_offered
from cf;


insert into ods_business_features (
    select
         business_id,
         name,
         address,
         city,
         state,
         postal_code,
         cast(latitude as float),
         cast(longitude as float),
         cast(stars as float),
         cast(review_count as int),
         CASE WHEN is_open = '0' THEN false ELSE true END as is_open
    from business
);

select * from ods_covid_features;
select * from ods_business_features;