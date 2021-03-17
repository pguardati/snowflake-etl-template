import os
import pandas as pd

from src.constants import DIR_DATA, DIR_DATA_TEST


def sample_dataset(dataset_path):
    """Sample and store a dataset

    Args:
        dataset_path(str): dataset path respect to DIR_DATA

    """
    number_of_elements = 100
    input_file = os.path.join(DIR_DATA, dataset_path)
    output_file = os.path.join(DIR_DATA_TEST, dataset_path)
    os.makedirs(os.path.dirname(output_file), exist_ok=True)

    # sample and store file in test directory
    extension = dataset_path.split(".")[-1]
    if extension == "csv":
        df_climate_temp = pd.read_csv(
            input_file,
            nrows=number_of_elements
        )
        df_climate_temp.to_csv(output_file, index=False)
    elif extension == "json":
        df = pd.read_json(
            input_file,
            nrows=number_of_elements,
            lines=True
        )
        df.to_json(
            output_file,
            orient="records"
        )

    print(f"storing dataset in {output_file}")


def sample_reviews(dataset_path):
    number_of_elements = 100
    input_file = os.path.join(DIR_DATA, dataset_path)
    output_file = os.path.join(DIR_DATA_TEST, dataset_path)
    os.makedirs(os.path.dirname(output_file), exist_ok=True)

    # sample and store file in test directory
    df = pd.read_json(
        input_file,
        nrows=number_of_elements,
        lines=True
    )
    df.to_json(
        output_file,
        orient="records"
    )
    reviews_id = list(df["review_id"].values)
    business_id = list(df["business_id"].values)
    user_id = list(df["user_id"].values)
    date = list(df["date"].values)
    return reviews_id, business_id, user_id, date


#
# def main():
#     """create test data"""
#
#
# if __name__ == "__main__":
#     main()


reviews_path = "yelp_dataset/yelp_academic_dataset_review.json"
reviews_id, business_id, user_id, date = sample_reviews(reviews_path)
datasets = [
    "climate_explorer/USC00420849-BOULDER-precipitation-inch.csv",
    "climate_explorer/USC00420849-temperature-degreeF.csv",
    "covid_19_dataset_2020_06_10/yelp_academic_dataset_covid_features.json",
    "yelp_dataset/yelp_academic_dataset_business.json",
    "yelp_dataset/yelp_academic_dataset_checkin.json",
    "yelp_dataset/yelp_academic_dataset_tip.json",
    "yelp_dataset/yelp_academic_dataset_user.json"
]