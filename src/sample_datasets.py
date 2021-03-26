import os
import pandas as pd

from src.constants import DIR_DATA_TEST, DIR_DATA

datasets = {
    "reviews": "yelp_dataset/yelp_academic_dataset_review.json",
    "precipitations": "climate_explorer/USC00420849-BOULDER-precipitation-inch.csv",
    "temperatures": "climate_explorer/USC00420849-temperature-degreeF.csv",
    "tips": "yelp_dataset/yelp_academic_dataset_tip.json",
    "users": "yelp_dataset/yelp_academic_dataset_user.json",
    "covid_features": "covid_19_dataset_2020_06_10/yelp_academic_dataset_covid_features.json",
    "business_features": "yelp_dataset/yelp_academic_dataset_business.json",
    "checkins": "yelp_dataset/yelp_academic_dataset_checkin.json"
}


def read_data(number_of_elements):
    dataframes = {}
    for table, dataset_path in datasets.items():
        extension = dataset_path.split(".")[-1]
        if extension == "csv":
            df = pd.read_csv(os.path.join(DIR_DATA, dataset_path),
                             nrows=number_of_elements)
        elif extension == "json":
            df = pd.read_json(os.path.join(DIR_DATA, dataset_path),
                              nrows=number_of_elements, lines=True)
        dataframes[table] = df
    return dataframes


def process_data(dataframes):
    df_reviews = dataframes["reviews"]

    business_ids = list(df_reviews.business_id)
    user_ids = list(df_reviews.user_id)
    dates = list(df_reviews.date)

    # adapt tips
    dataframes["tips"]["business_id"] = business_ids
    dataframes["tips"]["user_id"] = user_ids
    dataframes["tips"]["date"] = dates

    # adapt date models
    dataframes["precipitations"]["date"] = dates
    dataframes["temperatures"]["date"] = dates

    # adapt user
    dataframes["users"]["user_id"] = user_ids

    # adapt business fields
    dataframes["covid_features"]["business_id"] = business_ids
    dataframes["business_features"]["business_id"] = business_ids
    dataframes["checkins"]["business_id"] = business_ids
    return dataframes


def export_data(dataframes):
    for table, df in dataframes.items():
        # create output directory
        path = datasets[table]
        file_output = os.path.join(DIR_DATA_TEST, path)
        dir_output = os.path.dirname(file_output)
        os.makedirs(dir_output, exist_ok=True)
        print(f"store {table} data in {file_output}")
        # process and store file
        extension = path.split(".")[-1]
        if extension == "csv":
            df.to_csv(os.path.join(DIR_DATA_TEST, path), index=None,
                      date_format='%Y%m%d')
        elif extension == "json":
            df.to_json(os.path.join(DIR_DATA_TEST, path), orient="records",
                       date_format="iso", lines=True)


def main():
    number_of_elements = 10
    dataframes = read_data(number_of_elements)
    dataframes = process_data(dataframes)
    export_data(dataframes)


if __name__ == "__main__":
    main()
