import os
from tabulate import tabulate
import snowflake.connector
import pandas as pd

from src.constants import \
    SNOWFLAKE_USER, SNOWFLAKE_ACCOUNT, SNOWFLAKE_PASSWORD, \
    SNOWFLAKE_DB_NAME, DIR_DATA_TEST, DIR_DATA


def get_files_information(dir_data):
    """Read file dimensions"""
    file_list = []
    for path, subdirs, files in os.walk(dir_data):
        for name in files:
            if name.endswith("json") or name.endswith("csv"):
                file = os.path.join(path, name)
                file_list.append((file, os.stat(file).st_size))
    df_files = pd.DataFrame(file_list, columns=["FILE_NAME", "RAW"])
    df_files["TABLE_NAME"] = [
        "CHECKINS",
        "TIPS",
        "REVIEWS",
        "BUSINESS_FEATURES",
        "USERS",
        "PRECIPITATIONS",
        "TEMPERATURES",
        "COVID_FEATURES"
    ]
    return df_files


def main(dir_data=DIR_DATA_TEST):
    """Compare raw file size with staged and ods models"""
    conn = snowflake.connector.connect(
        user=SNOWFLAKE_USER,
        password=SNOWFLAKE_PASSWORD,
        account=SNOWFLAKE_ACCOUNT
    )

    cur = conn.cursor()
    cur.execute(f"""use database {SNOWFLAKE_DB_NAME};""")
    cur.execute("""use schema INFORMATION_SCHEMA;""")

    df_files = get_files_information(dir_data)

    # get table dimension
    df_staging = pd.read_sql("""
        SELECT table_schema, table_name,bytes
        FROM  information_schema.tables
        WHERE table_schema='STAGING'
    """, conn).rename(columns={"BYTES": "STAGING"})

    df_ods = pd.read_sql("""
        SELECT table_schema, table_name,bytes
        FROM  information_schema.tables
        WHERE table_schema='ODS'
    """, conn).rename(columns={"BYTES": "ODS"})

    # merge file and table dimension
    df = df_files \
        .merge(df_staging, on="TABLE_NAME", how="outer") \
        .merge(df_ods, on="TABLE_NAME", how="outer") \
        [["FILE_NAME", "TABLE_NAME", "RAW", "STAGING", "ODS"]]
    print(tabulate(df, headers=df.columns, tablefmt="psql"))


if __name__ == "__main__":
    main()
