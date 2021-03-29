import sys
import argparse
from subprocess import call
from src.etl import stage_upload_data


def main(args=None):
    # parse arguments
    parser = argparse.ArgumentParser(
        description="Orchestrate etl pipelines to store, clean "
                    "and transfer data in a snowflake data warehouse")
    parser.add_argument("--db-name")
    parser.add_argument("--dir-scripts")
    parser.add_argument("--dir-data")
    args = args or sys.argv[1:]
    args = parser.parse_args(args)
    print(f"Using database {args.db_name}")
    print(f"Using scripts from {args.dir_scripts}")

    # create schemas
    _ = call(
        f"""
        snowsql -d {args.db_name} \
        -f {args.dir_scripts}/stage_ddl.sql \
        -f {args.dir_scripts}/ods_ddl.sql \
        -f {args.dir_scripts}/dwh_ddl.sql 
        """,
        shell=True
    )

    # transfer data: stage -> ods -> dwh
    _ = call(
        f"""
        snowsql -d {args.db_name} \
        -f {args.dir_scripts}/stage_etl.sql \
        -f {args.dir_scripts}/ods_etl.sql \
        -f {args.dir_scripts}/dwh_etl.sql
        """,
        shell=True
    )
    _ = call(
        f"""
        snowsql -d {args.db_name} \
        -f {args.dir_scripts}/dwh_query.sql
        """,
        shell=True
    )


if __name__ == "__main__":
    main()
