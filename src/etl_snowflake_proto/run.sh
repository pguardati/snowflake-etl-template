# Creation
snowsql -f reset_db.sql

# Staging
python staging_create_staging_area.py
python staging_upload_json.py
python staging_upload_csv.py

# ODS
snowsql \
-d snowflake_db -s ods \
-f ods_ddl.sql \
-f ods_etl_weather.sql \
-f ods_etl_business.sql \
-f ods_etl_date.sql \
-f ods_etl_users.sql

# DWH
snowsql \
-d snowflake_db -s dwh \
-f dwh_ddl.sql \
-f dwh_etl.sql

# Business Query
snowsql -d snowflake_db -s dwh -f dwh_query.sql
