# snowflake-etl-template


# Setup snowflake
Insert credentials `~/.snowsql/config`
Copy config in `config/snowflake.config`


# Test
```
python tests/create_test_data.py
cd etl_snowflake
sh exe.sh
```

# Partition big datasets
```
python src/split_json_file.py \
--rel-path-file=yelp_dataset/yelp_academic_dataset_user.json \
--chunk-size=100000


python src/split_json_file.py \
--rel-path-file=yelp_dataset/yelp_academic_dataset_review.json \
--chunk-size=250000
```
