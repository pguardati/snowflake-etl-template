import os
import sys
import argparse
from subprocess import call

from src.constants import PROJECT_PATH

SCRIPTS_PATH = os.path.join(PROJECT_PATH, "src", "etl")


def main(args=None):
    # parse arguments
    parser = argparse.ArgumentParser(
        description="Orchestrate etl pipelines to store, clean "
                    "and transfer data in a snowflake data warehouse")
    parser.add_argument("--db-name")
    parser.add_argument("--dir-data")
    args = args or sys.argv[1:]
    args = parser.parse_args(args)
    print(f"Using database {args.db_name}")

    # create schemas
    _ = call(
        f"""
        snowsql -d {args.db_name} \
        -f {SCRIPTS_PATH}/stage_ddl.sql \
        -f {SCRIPTS_PATH}/ods_ddl.sql \
        -f {SCRIPTS_PATH}/dwh_ddl.sql 
        """,
        shell=True
    )

    # transfer data: stage -> ods -> dwh
    _ = call(
        f"""
        snowsql -d {args.db_name} \
        -f {SCRIPTS_PATH}/stage_etl.sql \
        -f {SCRIPTS_PATH}/ods_etl.sql \
        -f {SCRIPTS_PATH}/dwh_etl.sql
        """,
        shell=True
    )
    _ = call(
        f"""
        snowsql -d {args.db_name} \
        -f {SCRIPTS_PATH}/dwh_query.sql
        """,
        shell=True
    )


if __name__ == "__main__":
    main()
