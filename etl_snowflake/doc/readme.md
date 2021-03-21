# Setup snowflake 
Insert credentials `~/.snowsql/config`
Copy config in `config/snowflake.config`

```
```
# Staging
```
snowsql -f reset_db.sql
python staging_create_staging_area.py
python staging_upload_json.py
python staging_upload_csv.py
```

# ODS
```
snowsql -f ods_ddl.sql
snowsql -f ods_etl_weather.sql
snowsql -f ods_etl_business.sql
snowsql -f ods_etl_date.sql
snowsql -f ods_etl_users.sql
```

# DWH
```
snowsql -f dwh_ddl.sql
snowsql -f dwh_etl.sql
snowsql -f dwh_query.sql
``` 

