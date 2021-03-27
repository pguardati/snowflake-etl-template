snowsql -f reset_db.sql

# stage data
snowsql -f stage_ddl.sql
python stage_upload_data.py
snowsql -f stage_etl.sql

# ods creation and etl from staging
snowsql \
-f ods_ddl.sql \
-f ods_etl.sql \
-f dwh_ddl_etl.sql