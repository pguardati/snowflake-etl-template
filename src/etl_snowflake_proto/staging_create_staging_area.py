import snowflake.connector

from src.etl_snowflake_proto.staging_utils import create_staging_area
from src.constants import \
    SNOWFLAKE_USER, SNOWFLAKE_ACCOUNT, SNOWFLAKE_PASSWORD, \
    SNOWFLAKE_DB_NAME, SNOWFLAKE_STAGING_CSV, SNOWFLAKE_STAGING_JSON


def main():
    conn = snowflake.connector.connect(
        user=SNOWFLAKE_USER,
        password=SNOWFLAKE_PASSWORD,
        account=SNOWFLAKE_ACCOUNT
    )

    create_staging_area(
        conn,
        db_name=SNOWFLAKE_DB_NAME,
        json_staging_area_name=SNOWFLAKE_STAGING_CSV,
        csv_staging_area_name=SNOWFLAKE_STAGING_JSON,
    )


if __name__ == "__main__":
    main()
