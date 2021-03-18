import os
import pandas as pd

from src.constants import DIR_DATA, DIR_DATA_TEST


# def sample_dataset(dataset_path, target_data, target_column):
#     """Sample and store a dataset
#
#     Args:
#         dataset_path(str): dataset path respect to DIR_DATA
#
#     """
#     input_file = os.path.join(DIR_DATA, dataset_path)
#     output_file = os.path.join(DIR_DATA_TEST, dataset_path)
#     os.makedirs(os.path.dirname(output_file), exist_ok=True)
#
#     # sample and store file in test directory
#     extension = dataset_path.split(".")[-1]
#     if extension == "csv":
#         df = pd.read_csv(
#             input_file,
#         )
#         df.to_csv(output_file, index=False)
#     elif extension == "json":
#         df = pd.read_json(
#             input_file,
#             lines=True
#         )
#         df.to_json(
#             output_file,
#             orient="records"
#         )
#
#     print(f"storing dataset in {output_file}")


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


def sample_weather_data(dataset_path, dates, number_of_elements=100):
    input_file = os.path.join(DIR_DATA, dataset_path)
    output_file = os.path.join(DIR_DATA_TEST, dataset_path)
    os.makedirs(os.path.dirname(output_file), exist_ok=True)

    df = pd.read_csv(input_file)
    # get dates that matches reviews dates
    df_date = pd.DatetimeIndex(dates).strftime('%Y%m%d')
    target_dates = list(df_date.astype(int).values)
    df = df[df.date.isin(target_dates)]
    number_of_elements = len(df) if (len(df) < number_of_elements) \
        else number_of_elements
    # get maximum elements
    df = df.sample(number_of_elements)
    df.to_csv(output_file, index=False)
    return df


def sample_business_data(dataset_path, business_ids, number_of_elements=100):
    input_file = os.path.join(DIR_DATA, dataset_path)
    output_file = os.path.join(DIR_DATA_TEST, dataset_path)
    os.makedirs(os.path.dirname(output_file), exist_ok=True)

    df = pd.read_json(input_file, lines=True)
    # get dates that matches reviews dates
    df = df[df.business_id.isin(business_ids)]
    # get maximum elements
    number_of_elements = len(df) if (len(df) < number_of_elements) \
        else number_of_elements
    df = df.sample(number_of_elements)
    df.to_json(output_file, orient="records")
    return df


def sample_random_json_data(dataset_path, number_of_elements=100):
    input_file = os.path.join(DIR_DATA, dataset_path)
    output_file = os.path.join(DIR_DATA_TEST, dataset_path)
    os.makedirs(os.path.dirname(output_file), exist_ok=True)
    df = pd.read_json(input_file, lines=True, nrows=number_of_elements)
    df.to_json(output_file, orient="records")
    return df


#
# def main():
#     """create test data"""
#
#
# if __name__ == "__main__":
#     main()


reviews_path = "yelp_dataset/yelp_academic_dataset_review.json"
reviews_ids, business_ids, user_ids, dates = sample_reviews(reviews_path)
datasets = [
    "climate_explorer/USC00420849-BOULDER-precipitation-inch.csv",
    "climate_explorer/USC00420849-temperature-degreeF.csv",
    "covid_19_dataset_2020_06_10/yelp_academic_dataset_covid_features.json",
    "yelp_dataset/yelp_academic_dataset_business.json",
    "yelp_dataset/yelp_academic_dataset_checkin.json",
    "yelp_dataset/yelp_academic_dataset_tip.json",
    "yelp_dataset/yelp_academic_dataset_user.json"
]

_ = sample_weather_data(datasets[0], dates)
_ = sample_weather_data(datasets[1], dates)
df = sample_business_data(datasets[2], business_ids) # TODO -> this is empty, no common ids with reviews?
df = sample_business_data(datasets[3], business_ids)
_ = sample_random_json_data(datasets[4])
_ = sample_random_json_data(datasets[6])

# sample json by business_id
dataset_path = datasets[4]
number_of_elements = 100

# TODO1: fix business id (2), fix user_id (7), encapsulate and use