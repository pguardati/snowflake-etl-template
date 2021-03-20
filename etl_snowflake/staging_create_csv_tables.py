import snowflake.connector

from src.constants import \
    SNOWFLAKE_USER, SNOWFLAKE_ACCOUNT, SNOWFLAKE_PASSWORD, \
    SNOWFLAKE_DB_NAME, SNOWFLAKE_STAGING_CSV


def create_csv_staging_area_and_tables(
        conn,
        db_name,
        staging_area_name
):
    cur = conn.cursor()
    print("Creating csv staging area..")
    cur.execute(
        """
        use database {};
        """.format(db_name)
    )
    cur.execute(
        """
        create or replace file format csv_records
        type = csv 
        FIELD_DELIMITER = ',' 
        RECORD_DELIMITER = '\n' 
        skip_header = 1 
        null_if = ('NULL', 'null') 
        empty_field_as_null = true 
        compression = gzip 
        error_on_column_count_mismatch=false;
        """
    )
    cur.execute(
        """
        create or replace stage {}
        file_format= csv_records;
        """.format(staging_area_name)
    )

    print(f"Creating csv staging tables..")
    cur.execute(
        """
        drop table if exists precipitations
        """
    )
    cur.execute(
        """
        drop table if exists temperatures
        """
    )
    cur.execute(
        """
        create table precipitations (
             date timestamp,
             precipitation float,
             precipitation_normal float
        );
        """
    )
    cur.execute(
        """
        create table temperatures (
             date timestamp,
             min float,
             max float,
             normal_min float,
             normal_max float
        );
        """
    )


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
