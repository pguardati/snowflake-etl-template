import snowflake.connector

from etl_snowflake.staging_utils import create_csv_staging_area_and_tables
from src.constants import \
    SNOWFLAKE_USER, SNOWFLAKE_ACCOUNT, SNOWFLAKE_PASSWORD, \
    SNOWFLAKE_DB_NAME, SNOWFLAKE_STAGING_CSV


def main():
    conn = snowflake.connector.connect(
        user=SNOWFLAKE_USER,
        password=SNOWFLAKE_PASSWORD,
        account=SNOWFLAKE_ACCOUNT
    )
    create_csv_staging_area_and_tables(
        conn,
        staging_area_name=SNOWFLAKE_STAGING_CSV,
        db_name=SNOWFLAKE_DB_NAME,
    )


if __name__ == "__main__":
    main()
