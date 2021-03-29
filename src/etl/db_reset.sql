!set variable_substitution=true;
DROP DATABASE IF EXISTS &{DB_NAME};
CREATE DATABASE &{DB_NAME};
-- create stages
CREATE SCHEMA staging;
CREATE SCHEMA ods;
CREATE SCHEMA dwh;
-- create area for temporary files
USE SCHEMA staging;
-- json staging files
CREATE FILE format json_records TYPE = 'JSON' strip_outer_array = TRUE;
CREATE stage file_json file_format = json_records;
-- csv staging files
CREATE FILE format csv_records TYPE = csv FIELD_DELIMITER = ',' RECORD_DELIMITER = '\n'
skip_header = 1 null_if = ('NULL', 'null') empty_field_as_null = TRUE
compression = gzip error_on_column_count_mismatch = false;
CREATE stage file_csv file_format = csv_records;
