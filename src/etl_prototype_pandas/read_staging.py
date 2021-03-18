import os
import pandas as pd
from src.constants import DIR_DATA_TEST


def read_data():
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

    df_list = []
    for dataset_path, table in zip(datasets, table_names):
        extension = dataset_path.split(".")[-1]
        if extension == "csv":
            df = pd.read_csv(os.path.join(DIR_DATA_TEST, dataset_path))
        elif extension == "json":
            df = pd.read_json(os.path.join(DIR_DATA_TEST, dataset_path))
        df_list.append(df)
    return df_list, table_names
