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
    CASE WHEN delivery_or_takeout = 'TRUE' THEN true ELSE false END as delivery_or_takeout,
    CASE WHEN grubhub_enabled = 'TRUE' THEN true ELSE false END as grubhub_enabled,
    CASE WHEN call_to_action_enabled = 'TRUE' THEN true ELSE false END as call_to_action_enabled,
    CASE WHEN request_a_quote_enabled = 'TRUE' THEN true ELSE false END as request_a_quote_enabled,
    CASE WHEN temporary_closed_until = 'TRUE' THEN true ELSE false END as temporary_closed_until,
    CASE WHEN virtual_services_offered = 'TRUE' THEN true ELSE false END as virtual_services_offered
from cf

select * from ods_covid_features;