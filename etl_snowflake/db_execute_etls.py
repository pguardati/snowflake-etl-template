import sys
import argparse
from subprocess import call
from etl_snowflake import stage_upload_data


def main(args=None):

    # parse arguments
    parser = argparse.ArgumentParser(
        description="Orchestrate etl pipelines to store, clean "
                    "and transfer data in a snowflake data warehouse")
    parser.add_argument("--db-name")
    parser.add_argument("--dir-data")
    parser.add_argument("--dir-scripts")
    args = args or sys.argv[1:]
    args = parser.parse_args(args)
    print(f"Using database {args.db_name}")
    print(f"Using scripts from {args.dir_data}")
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

    # stage data
    stage_upload_data.main([
        f"--db-name={args.db_name}",
        f"--dir-data={args.dir_data}"
    ])

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


if __name__ == "__main__":
    main()
