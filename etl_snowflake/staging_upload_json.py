import snowflake.connector

from etl_snowflake.staging_utils import stage_data, create_json_staging_tables
from src.constants import \
    SNOWFLAKE_USER, SNOWFLAKE_ACCOUNT, SNOWFLAKE_PASSWORD, \
    SNOWFLAKE_DB_NAME, SNOWFLAKE_STAGING_JSON, \
    DIR_DATA_TEST


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
    create_json_staging_tables(conn, table_names)
    stage_data(
        conn,
        table_names,
        datasets,
        db_name=SNOWFLAKE_DB_NAME,
        staging_area_name=SNOWFLAKE_STAGING_JSON,
        staging_format="json_records",
        dir_datasets=DIR_DATA_TEST
    )


if __name__ == "__main__":
    main()
