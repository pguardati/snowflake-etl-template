import os
import pandas as pd

from src.constants import DIR_DATA_TEST

len_field = 10000
delimiter = "\""


def create_delete_ddl_statement(table_name, *args):
    "create delete statement"
    print(f"drop table if exists {table_name};")


def create_create_ddl_statement(table_name, df):
    "create create statement"
    # add header
    print(f"create table {table_name} (")
    # add fields
    columns = list(df.columns)
    separator = ","
    for i, col in enumerate(columns):
        if i == len(columns) - 1:
            separator = ""
        print(
            f"\t {delimiter}{col}{delimiter} varchar{separator}")
    # add bottom line
    print(");")


def create_insert_ddl_statement(table_name, df):
    "create insert statement"
    # add header
    print(f"cmd_insert_{table_name}=\"\"\"")
    print(f"insert into {table_name} (")
    # add fields
    columns = list(df.columns)
    separator = ","
    for i, col in enumerate(columns):
        if i == len(columns) - 1:
            separator = ""
        print(f"\t {delimiter}{col}{delimiter}{separator}")
    # add bottom line
    print(")")
    print("values (", end="")
    for j in range(len(df.columns)):
        if j < len(columns) - 1:
            print("%s,", end=" ")
        else:
            print("%s);", end=" ")
    print("\n\"\"\"\n")


def create_full_query_statement(table_name, *args):
    print(f"select * from {table_name};")


def create_ddl_statements(datasets, table_names, ddl_statement_function):
    for dataset_path, table_name in zip(datasets, table_names):
        extension = dataset_path.split(".")[-1]
        if extension == "csv":
            df = pd.read_csv(os.path.join(DIR_DATA_TEST, dataset_path))
        elif extension == "json":
            df = pd.read_json(os.path.join(DIR_DATA_TEST, dataset_path))
        ddl_statement_function(table_name, df)


def main():
    datasets = [
        "climate_explorer/USC00420849-BOULDER-precipitation-inch.csv",
        "climate_explorer/USC00420849-temperature-degreeF.csv",
        "covid_19_dataset_2020_06_10/yelp_academic_dataset_covid_features.json",
        # flatten highlights and covid banner
        "yelp_dataset/yelp_academic_dataset_business.json",
        # flatten hours, categories, attributes
        "yelp_dataset/yelp_academic_dataset_checkin.json",
        # flatten date
        "yelp_dataset/yelp_academic_dataset_review.json",
        "yelp_dataset/yelp_academic_dataset_tip.json",
        "yelp_dataset/yelp_academic_dataset_user.json"
        # flatten elite, friends

    ]

    table_names = [
        "precipitations",
        "temperatures",
        "covid_features",
        "business",
        "checkins",
        "reviews",
        "tips",
        "users"
    ]

    print("\"\"\"FULL QUERIES\"\"\"")
    print("\ncmd_query_tables=\"\"\"")
    create_ddl_statements(datasets, table_names, create_full_query_statement)
    print("\"\"\"\n")

    print("\"\"\"DELETE QUERIES\"\"\"")
    print("cmd_delete_tables=\"\"\"")
    create_ddl_statements(datasets, table_names, create_delete_ddl_statement)
    print("\"\"\"\n")

    print("\"\"\"CREATE QUERIES\"\"\"")
    print("\ncmd_create_tables=\"\"\"")
    create_ddl_statements(datasets, table_names, create_create_ddl_statement)
    print("\"\"\"\n")

    print("\"\"\"INSERT QUERIES\"\"\"")
    print("")
    create_ddl_statements(datasets, table_names, create_insert_ddl_statement)
    print("")


if __name__ == "__main__":
    """
    python create_staging_ddl.py > staging_cmd.py
    """
    main()
