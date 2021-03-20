import os

from src.constants import DIR_DATA_TEST


def create_staging_area(
        conn,
        db_name,
        json_staging_area_name,
        csv_staging_area_name
):
    cur = conn.cursor()
    cur.execute(
        """
        use database {};
        """.format(db_name)
    )

    print("Creating json staging area..")
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
        """.format(json_staging_area_name)
    )

    print("Creating csv staging area..")
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
        """.format(csv_staging_area_name)
    )


def create_json_staging_tables(
        conn,
        table_names,
):
    cur = conn.cursor()
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


def create_csv_staging_tables(
        conn
):
    cur = conn.cursor()

    print(f"Creating csv staging tables:"
          f"precipitations and temperatures")
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
             date int,
             precipitation float,
             precipitation_normal float
        );
        """
    )
    cur.execute(
        """
        create table temperatures (
             date int,
             min float,
             max float,
             normal_min float,
             normal_max float
        );
        """
    )


def stage_data(
        conn,
        table_names,
        datasets,
        db_name,
        staging_area_name,
        staging_format,
        dir_datasets
):
    """upload to staging area, copy from staging into tables"""
    cur = conn.cursor()
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
            file_format = (format_name = {staging_format})
            on_error = 'skip_file';
            """
        )
        print("response: ", cur.fetchall())
