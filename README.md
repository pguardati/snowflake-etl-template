# snowflake-etl-template
Scripts to transfer and process data to snowflake.

# Setup snowflake

Insert credentials `~/.snowsql/config`
Copy configuration variables in `config/snowflake.config` with format:
```
[SNOWFLAKE]
user=..
password=..
account=..
```

# Test

```
# create test set
python tests/transform_to_test_data.py

# run tests
python discover -u tests
```

# Usage

## Partition big datasets

```
# split user dataset
python src/split_json_file.py \
--rel-path-file=yelp_dataset/yelp_academic_dataset_user.json \
--chunk-size=100000

# split review dataset
python src/split_json_file.py \
--rel-path-file=yelp_dataset/yelp_academic_dataset_review.json \
--chunk-size=250000
```

## Run the etl

```
# create a new database
#snowsql -f etl_snowflake/db_reset.sql -D DB_NAME=snowflake_db

# run the etl on real dataset
python etl_snowflake/db_execute_etls.py \
--db-name=snowflake_db \
--dir-scripts=/Users/pietroguardati/PycharmProjects/snowflake-etl-template/etl_snowflake 
# --dir-data=/Users/pietroguardati/data/snowflake_data 

# compare dimension of raw files vs uploaded files
python etl_snowflake/stage_dim_comparison.py \
--db-name=snowflake_db \
--dir-data=/Users/pietroguardati/data/snowflake_data 
```
