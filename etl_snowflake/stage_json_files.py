import os
import snowflake.connector

import pandas as pd
from tabulate import tabulate

from src.constants import \
    SNOWFLAKE_USER, SNOWFLAKE_ACCOUNT, SNOWFLAKE_PASSWORD, \
    DIR_DATA, DIR_DATA_TEST

cmd_use_staging_db = """
use database {};
"""
cmd_create_json_parser = """
create or replace file format json_records 
type = 'JSON' 
strip_outer_array=true;
"""
cmd_create_json_staging = """
create or replace stage {}
file_format=json_records;
"""

cmd_delete_staging_table = """
drop table if exists {};
"""
cmd_create_staging_table = """
create table {} (json_records variant);
"""

cmd_upload_file = """
put file://{} @{} auto_compress=true;
"""
cmd_copy_staging_to_staging_table = """
copy into {} from @{}/{}.gz 
file_format = (format_name = json_records);
"""

# connect
# TODO: remove sensitive data
conn = snowflake.connector.connect(
    user=SNOWFLAKE_USER,
    password=SNOWFLAKE_PASSWORD,
    account=SNOWFLAKE_ACCOUNT
)
cur = conn.cursor()

file_name = "covid_19_dataset_2020_06_10/yelp_academic_dataset_covid_features.json"
table_name = "covid_features"

# create staging
cur.execute(cmd_use_staging_db.format("snowflake_db"))
cur.execute(cmd_create_json_parser)
cur.execute(cmd_create_json_staging.format("test_staging_area"))

# reset staging tables tables
cur.execute(cmd_delete_staging_table.format(table_name))
cur.execute(cmd_create_staging_table.format(table_name))

# upload a file
file_path = os.path.join(DIR_DATA_TEST, file_name)
cur.execute(cmd_upload_file.format(file_path, "test_staging_area"))

print("content of the stage:")
cur.execute("list @test_staging_area")
cur.fetchall()

# transfer file from staging area to staging table
cur.execute(
    cmd_copy_staging_to_staging_table.format(
        table_name,
        "test_staging_area",
        os.path.basename(file_path)
    )
)
print(cur.fetchall())

df = pd.read_sql("select * from covid_features", conn)
# print(tabulate(df,headers=df.columns,tablefmt="psql"))
