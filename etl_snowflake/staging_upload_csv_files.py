import snowflake.connector

from etl_snowflake.staging_upload_json_files import stage_data
from src.constants import \
    SNOWFLAKE_USER, SNOWFLAKE_ACCOUNT, SNOWFLAKE_PASSWORD, \
    SNOWFLAKE_DB_NAME, SNOWFLAKE_STAGING_CSV, \
    DIR_DATA, DIR_DATA_TEST


def main():
    table_names = [
        "temperatures",
        "precipitations"
    ]

    datasets = [
        "climate_explorer/USC00420849-BOULDER-precipitation-inch.csv",
        "climate_explorer/USC00420849-temperature-degreeF.csv",
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
        staging_area_name=SNOWFLAKE_STAGING_CSV,
        staging_format="csv_records",
        dir_datasets=DIR_DATA_TEST
    )


if __name__ == "__main__":
    main()
