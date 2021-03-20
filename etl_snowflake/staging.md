reset database
```
snowsql
drop database snowflake_db;
create database snowflake_db;
```
create tables
```
python etl_snowflake/staging_create_staging_area.py
```
upload files
```
python etl_snowflake/staging_upload_json.py
python etl_snowflake/staging_upload_csv.py
```