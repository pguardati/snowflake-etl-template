import os
import pandas as pd

from src.constants import DIR_DATA_TEST


def create_delete_ddl_statement(table_name):
    "create delete statement"
    print(f"delete table if exists {table_name}")


def create_create_ddl_statement(df, table_name):
    "create create statement"
    # add header
    print(f"create table {table_name} (")
    # add fields
    columns = list(df.columns)
    separator = ","
    for i, col in enumerate(columns):
        if i == len(columns) - 1:
            separator = ""
        print(f"\t '{col}' varchar(1000){separator}")
    # add bottom line
    print(")")


def create_insert_ddl_statement(df, table_name):
    "create insert statement"
    # add header
    print(f"insert into {table_name} (")
    # add fields
    columns = list(df.columns)
    separator = ","
    for i, col in enumerate(columns):
        if i == len(columns) - 1:
            separator = ""
        print(f"\t '{col}'{separator}")
    # add bottom line
    print(")")
    print("values (", end="")
    for j in range(len(df.columns)):
        if j < len(columns) - 1:
            print("%s,", end=" ")
        else:
            print("%s)", end=" ")


def create_staging_ddl(df, table_name):
    print("")
    create_delete_ddl_statement(table_name)
    print("")
    create_create_ddl_statement(df, table_name)
    print("")
    create_insert_ddl_statement(df, table_name)
    print("")


def main():
    "create ddls for each dataset"

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

    for dataset_path, table in zip(datasets, table_names):
        extension = dataset_path.split(".")[-1]
        if extension == "csv":
            df = pd.read_csv(os.path.join(DIR_DATA_TEST, dataset_path))
        elif extension == "json":
            df = pd.read_json(os.path.join(DIR_DATA_TEST, dataset_path))
        create_staging_ddl(df, table_name="precipitations")


if __name__ == "__main__":
    main()
