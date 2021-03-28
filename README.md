# snowflake-etl-template

# Setup snowflake

Insert credentials `~/.snowsql/config`
Copy config in `config/snowflake.config`

# Test

```
# create test set
python tests/create_test_data.py
# run tests
python discover -u tests
```

# Usage

## Partition big datasets

```
python src/split_json_file.py \
--rel-path-file=yelp_dataset/yelp_academic_dataset_user.json \
--chunk-size=100000


python src/split_json_file.py \
--rel-path-file=yelp_dataset/yelp_academic_dataset_review.json \
--chunk-size=250000
```

## Run the etl

```
# create a new database
#snowsql -f etl_snowflake/db_reset.sql -D DB_NAME=snowflake_db

# run the etl
python etl_snowflake/db_execute_etls.py \
--db-name=snowflake_db \
--dir-data=/Users/pietroguardati/data/snowflake_data \
--dir-scripts=/Users/pietroguardati/PycharmProjects/snowflake-etl-template/etl_snowflake
```
