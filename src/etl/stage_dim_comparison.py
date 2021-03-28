import os
import sys
import argparse
from tabulate import tabulate
import snowflake.connector
import pandas as pd

from src.constants import SNOWFLAKE_USER, SNOWFLAKE_ACCOUNT, SNOWFLAKE_PASSWORD


def walklevel(some_dir, level=1):
    """os.walk with user-defined level of subdirectory exploration
    (imported from stack overflow)
    Args:
        some_dir(str): path of a directory
        level(int): maximum number of sub-directories levels to explore

    """
    some_dir = some_dir.rstrip(os.path.sep)
    assert os.path.isdir(some_dir)
    num_sep = some_dir.count(os.path.sep)
    for root, dirs, files in os.walk(some_dir):
        yield root, dirs, files
        num_sep_this = root.count(os.path.sep)
        if num_sep + level <= num_sep_this:
            del dirs[:]


def get_files_information(dir_data):
    """Read dimension of each dataset

    Args:
        dir_data(str): directory where the data are stored

    Returns:
        pd.DataFrame
    """
    file_list = []
    for path, subdirs, files in walklevel(dir_data, level=1):
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


def main(args=None):
    """Compare raw file size with staged and ods models"""
    # parse arguments
    args = args or sys.argv[1:]
    parser = argparse.ArgumentParser()
    parser.add_argument("--db-name", help="name of snowflake database")
    parser.add_argument("--dir-data", help="base directory of data files")
    args = parser.parse_args(args)

    # connect to the database
    conn = snowflake.connector.connect(
        user=SNOWFLAKE_USER,
        password=SNOWFLAKE_PASSWORD,
        account=SNOWFLAKE_ACCOUNT
    )
    cur = conn.cursor()
    cur.execute(f"""use database {args.db_name};""")
    cur.execute("""use schema INFORMATION_SCHEMA;""")

    df_files = get_files_information(args.dir_data)

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
