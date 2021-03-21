python staging_create_queries.py > staging_queries.py
python etl_staging.py

psql -f etl_stage2ods_ddl.sql -d test_snowflake
psql -f etl_stage2ods_business.sql -d test_snowflake
psql -f etl_stage2ods_date.sql -d test_snowflake
psql -f etl_stage2ods_users.sql -d test_snowflake
psql -f etl_stage2ods_weather.sql -d test_snowflake

psql -f etl_ods2dwh_ddl.sql -d test_snowflake
psql -f etl_ods2dwh.sql -d test_snowflake

psql -f etl_dwh_business_query.sql -d test_snowflake