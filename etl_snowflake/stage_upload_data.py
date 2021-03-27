import os
import sys
import argparse
import snowflake.connector

from src.constants import \
    SNOWFLAKE_USER, SNOWFLAKE_ACCOUNT, SNOWFLAKE_PASSWORD, \
    SNOWFLAKE_DB_NAME, SNOWFLAKE_STAGING_CSV, SNOWFLAKE_STAGING_JSON, \
    DIR_DATA_TEST, DIR_DATA


def get_partition_files(partition, dir_data):
    partition_path = os.path.join(dir_data, partition)
    files = os.listdir(partition_path)
    relative_files = [os.path.join(partition, file) for file in files]
    return relative_files


def upload_data(
        conn,
        datasets,
        staging_area_name,
        dir_datasets
):
    """upload to staging area, copy from staging into tables"""
    cur = conn.cursor()
    # upload data in staging area
    for dataset in datasets:
        print(f"Uploading {dataset} into staging")
        file_path = os.path.join(dir_datasets, dataset)
        cur.execute(
            f"""
            put file://{file_path} @{staging_area_name} auto_compress=true;
            """
        )
        print("response: ", cur.fetchall())


def parse_args(args):
    parser = argparse.ArgumentParser()
    parser.add_argument("--data-dir",
                        help="base directory of data files",
                        default=DIR_DATA_TEST)
    return parser.parse_args(args)


def main(args=None):
    args = args or sys.argv[1:]
    args = parse_args(args)
    print(f"Using data directory: {args.data_dir}")

    conn = snowflake.connector.connect(
        user=SNOWFLAKE_USER,
        password=SNOWFLAKE_PASSWORD,
        account=SNOWFLAKE_ACCOUNT
    )
    conn.cursor().execute(
        f"""
        use database {SNOWFLAKE_DB_NAME};
        """
    )
    conn.cursor().execute(
        f"""
        use schema staging;
        """
    )

    # get dataset files
    datasets_csv = [
        "climate_explorer/USC00420849-BOULDER-precipitation-inch.csv",
        "climate_explorer/USC00420849-temperature-degreeF.csv"
    ]
    datasets_json = [
        "covid_19_dataset_2020_06_10/yelp_academic_dataset_covid_features.json",
        "yelp_dataset/yelp_academic_dataset_business.json",
        "yelp_dataset/yelp_academic_dataset_checkin.json",
        "yelp_dataset/yelp_academic_dataset_tip.json",
    ]
    review_files = get_partition_files(
        "yelp_dataset/yelp_academic_dataset_review_partitioned",
        dir_data=args.data_dir
    )
    user_partitions = get_partition_files(
        "yelp_dataset/yelp_academic_dataset_user_partitioned",
        dir_data=args.data_dir
    )
    datasets_json = datasets_json + review_files + user_partitions

    # upload data
    upload_data(
        conn,
        datasets=datasets_csv,
        staging_area_name=SNOWFLAKE_STAGING_CSV,
        dir_datasets=args.data_dir
    )
    upload_data(
        conn,
        datasets=datasets_json,
        staging_area_name=SNOWFLAKE_STAGING_JSON,
        dir_datasets=args.data_dir
    )


if __name__ == "__main__":
    main()
