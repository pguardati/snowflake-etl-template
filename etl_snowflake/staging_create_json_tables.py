import snowflake.connector

from etl_snowflake.staging_utils import create_json_staging_area_and_tables
from src.constants import \
    SNOWFLAKE_USER, SNOWFLAKE_ACCOUNT, SNOWFLAKE_PASSWORD, \
    SNOWFLAKE_DB_NAME, SNOWFLAKE_STAGING_JSON


def main():
    table_names = [
        "covid_features",
        "business",
        "checkins",
        "reviews",
        "tips",
        "users"
    ]

    conn = snowflake.connector.connect(
        user=SNOWFLAKE_USER,
        password=SNOWFLAKE_PASSWORD,
        account=SNOWFLAKE_ACCOUNT
    )
    create_json_staging_area_and_tables(
        conn,
        table_names,
        staging_area_name=SNOWFLAKE_STAGING_JSON,
        db_name=SNOWFLAKE_DB_NAME,
    )


if __name__ == "__main__":
    main()
