# Staging
reset database
```
snowsql -f reset_db.sql
```
create tables
```
python staging_create_staging_area.py
```
upload files
```
python staging_upload_json.py
python staging_upload_csv.py
```

# ODS
```
snowsql -f ods_ddl.sql
snowsql -f ods_etl_weather.sql
snowsql -f ods_etl_business.sql
snowsql -f ods_etl_date.sql
```



