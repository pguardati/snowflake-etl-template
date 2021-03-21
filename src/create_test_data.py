import os
import pandas as pd

from src.constants import DIR_DATA, DIR_DATA_TEST


def sample_reviews(dataset_path, number_of_elements=100):
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

    print(f"exported {len(df)} elements in {dataset_path}")
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
    print(f"exported {len(df)} elements in {dataset_path}")
    return df


def sample_data_by_target(
        dataset_path,
        target_ids,
        target_column,
        number_of_elements=100
):
    input_file = os.path.join(DIR_DATA, dataset_path)
    output_file = os.path.join(DIR_DATA_TEST, dataset_path)
    os.makedirs(os.path.dirname(output_file), exist_ok=True)

    df = pd.read_json(input_file, lines=True, nrows=number_of_elements)
    # get dates that matches reviews dates
    df = df[df[target_column].isin(target_ids)]
    # get maximum elements
    number_of_elements = len(df) if (len(df) < number_of_elements) \
        else number_of_elements
    df.to_json(output_file, orient="records")
    print(f"exported {len(df)} elements in {dataset_path}")
    return df


def sample_random_json_data(dataset_path, number_of_elements=100):
    input_file = os.path.join(DIR_DATA, dataset_path)
    output_file = os.path.join(DIR_DATA_TEST, dataset_path)
    os.makedirs(os.path.dirname(output_file), exist_ok=True)
    df = pd.read_json(input_file, lines=True, nrows=number_of_elements)
    df.to_json(output_file, orient="records")
    print(f"exported {len(df)} elements in {dataset_path}")
    return df


def main():
    """create test data"""

    datasets = {
        "reviews": "yelp_dataset/yelp_academic_dataset_review.json",
        "precipitations": "climate_explorer/USC00420849-BOULDER-precipitation-inch.csv",
        "temperatures": "climate_explorer/USC00420849-temperature-degreeF.csv",
        "covid_features": "covid_19_dataset_2020_06_10/yelp_academic_dataset_covid_features.json",
        "business_features": "yelp_dataset/yelp_academic_dataset_business.json",
        "checkins": "yelp_dataset/yelp_academic_dataset_checkin.json",
        "tips": "yelp_dataset/yelp_academic_dataset_tip.json",
        "users": "yelp_dataset/yelp_academic_dataset_user.json"
    }

    # Sample reviews - datasets with all foreign keys of the future star schema
    reviews_ids, business_ids, user_ids, dates = sample_reviews(
        datasets["reviews"], number_of_elements=3000
    )

    # Sample data that matches the extracted keys from reviews
    _ = sample_weather_data(datasets["precipitations"], dates)
    _ = sample_weather_data(datasets["temperatures"], dates)

    _ = sample_data_by_target(
        datasets["business_features"], business_ids, "business_id")
    _ = sample_data_by_target(
        datasets["users"], user_ids, "user_id", number_of_elements=1000)

    # sample at random data excluded from star schema
    _ = sample_random_json_data(datasets["covid_features"])
    _ = sample_random_json_data(datasets["checkins"])
    _ = sample_random_json_data(datasets["tips"])


if __name__ == "__main__":
    main()
