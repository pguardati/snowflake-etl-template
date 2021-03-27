DIR_SCRIPTS=etl_snowflake
DB_NAME=$1
DATA_DIR=$2

echo "using database $DB_NAME"
echo "using data from $DATA_DIR"

# create stages
snowsql -d $DB_NAME \
-f $DIR_SCRIPTS/stage_ddl.sql

# stage data
python $DIR_SCRIPTS/stage_upload_data.py \
--db-name=$DB_NAME \
--dir-data=$DATA_DIR

# transfer data: stage -> ods -> dwh
snowsql -d $DB_NAME \
-f $DIR_SCRIPTS/stage_etl.sql \
-f $DIR_SCRIPTS/ods_ddl.sql \
-f $DIR_SCRIPTS/ods_etl.sql \
-f $DIR_SCRIPTS/dwh_ddl_etl.sql