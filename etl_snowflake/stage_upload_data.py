import os
import snowflake.connector

from src.constants import \
    SNOWFLAKE_USER, SNOWFLAKE_ACCOUNT, SNOWFLAKE_PASSWORD, \
    SNOWFLAKE_DB_NAME, SNOWFLAKE_STAGING_CSV, SNOWFLAKE_STAGING_JSON, \
    DIR_DATA_TEST


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


def main():
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
    datasets_csv = [
        "climate_explorer/USC00420849-BOULDER-precipitation-inch.csv",
        "climate_explorer/USC00420849-temperature-degreeF.csv"
    ]
    datasets_json = [
        "covid_19_dataset_2020_06_10/yelp_academic_dataset_covid_features.json",
        "yelp_dataset/yelp_academic_dataset_business.json",
        "yelp_dataset/yelp_academic_dataset_checkin.json",
        "yelp_dataset/yelp_academic_dataset_review.json",
        "yelp_dataset/yelp_academic_dataset_tip.json",
        "yelp_dataset/yelp_academic_dataset_user.json"
    ]
    upload_data(
        conn,
        datasets=datasets_csv,
        staging_area_name=SNOWFLAKE_STAGING_CSV,
        dir_datasets=DIR_DATA_TEST
    )
    upload_data(
        conn,
        datasets=datasets_json,
        staging_area_name=SNOWFLAKE_STAGING_JSON,
        dir_datasets=DIR_DATA_TEST
    )


if __name__ == "__main__":
    main()
