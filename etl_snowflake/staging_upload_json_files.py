import os
import snowflake.connector

from src.constants import \
    SNOWFLAKE_USER, SNOWFLAKE_ACCOUNT, SNOWFLAKE_PASSWORD, \
    SNOWFLAKE_DB_NAME, SNOWFLAKE_STAGING_JSON, \
    DIR_DATA, DIR_DATA_TEST


def stage_data(
        conn,
        table_names,
        datasets,
        db_name,
        staging_area_name,
        dir_datasets,
        staging_format
):
    """upload to staging area, copy from staging into tables"""
    cur = conn.cursor()

    cur.execute(
        f"""
        use database {db_name};
        """
    )

    for table_name, dataset in zip(table_names, datasets):
        print(f"Uploading {dataset} into staging")
        file_path = os.path.join(dir_datasets, dataset)
        cur.execute(
            f"""
            put file://{file_path} @{staging_area_name} auto_compress=true;
            """
        )
        print("response: ", cur.fetchall())

    for table_name, dataset in zip(table_names, datasets):
        print(f"Loading staging data into {table_name}")
        file_name = os.path.basename(os.path.join(DIR_DATA_TEST, dataset))
        cur.execute(
            f"""
            copy into {table_name} from @{staging_area_name}/{file_name}.gz 
            file_format = (format_name = {staging_format});
            """
        )
        print("response: ", cur.fetchall())


def main():
    table_names = [
        "covid_features",
        "business",
        "checkins",
        "reviews",
        "tips",
        "users"
    ]

    datasets = [
        "covid_19_dataset_2020_06_10/yelp_academic_dataset_covid_features.json",
        "yelp_dataset/yelp_academic_dataset_business.json",
        "yelp_dataset/yelp_academic_dataset_checkin.json",
        "yelp_dataset/yelp_academic_dataset_review.json",
        "yelp_dataset/yelp_academic_dataset_tip.json",
        "yelp_dataset/yelp_academic_dataset_user.json"
    ]

    conn = snowflake.connector.connect(
        user=SNOWFLAKE_USER,
        password=SNOWFLAKE_PASSWORD,
        account=SNOWFLAKE_ACCOUNT
    )

    stage_data(
        conn,
        table_names,
        datasets,
        db_name=SNOWFLAKE_DB_NAME,
        staging_area_name=SNOWFLAKE_STAGING_JSON,
        dir_datasets=DIR_DATA_TEST,
        staging_format="json_records"
    )


if __name__ == "__main__":
    main()
