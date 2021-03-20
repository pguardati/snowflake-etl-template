import snowflake.connector

from src.constants import \
    SNOWFLAKE_USER, SNOWFLAKE_ACCOUNT, SNOWFLAKE_PASSWORD, \
    SNOWFLAKE_DB_NAME, SNOWFLAKE_STAGING_JSON


def create_staging_area_and_tables(
        conn,
        table_names,
        db_name,
        staging_area_name
):
    cur = conn.cursor()
    print("Creating staging area..")
    cur.execute(
        """
        use database {};
        """.format(db_name)
    )
    cur.execute(
        """
        create or replace file format json_records 
        type = 'JSON' 
        strip_outer_array=true;
        """
    )
    cur.execute(
        """
        create or replace stage {}
        file_format=json_records;
        """.format(staging_area_name)
    )

    for table_name in table_names:
        print(f"Creating staging table: {table_name}..")
        cur.execute(
            """
            drop table if exists {};
            """.format(table_name)
        )
        cur.execute(
            """
            create table if not exists {} (json_records variant);
            """.format(table_name)
        )


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
    create_staging_area_and_tables(
        conn,
        table_names,
        staging_area_name=SNOWFLAKE_STAGING_JSON,
        db_name=SNOWFLAKE_DB_NAME,
    )


if __name__ == "__main__":
    main()
