snowsql \
-f reset_db.sql \
-f stage_ddl.sql
python stage_upload_data.py
snowsql \
-f stage_etl.sql \
-f ods_ddl.sql