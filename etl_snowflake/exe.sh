snowsql \
-f reset_db.sql \
-f stage_ddl.sql
python stage_upload_data.py
