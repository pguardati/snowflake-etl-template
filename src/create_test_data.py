import os
import pandas as pd

from src.constants import DIR_DATA, DIR_DATA_TEST


def sample_reviews(
        dataset_path,
        list_of_users,
        number_of_loaded_elements=100,
        number_of_exported_elements=100
):
    input_file = os.path.join(DIR_DATA, dataset_path)
    output_file = os.path.join(DIR_DATA_TEST, dataset_path)
    os.makedirs(os.path.dirname(output_file), exist_ok=True)

    # sample reviews based on users
    df = pd.read_json(
        input_file,
        nrows=number_of_loaded_elements,
        lines=True
    )
    df = df[df["user_id"].isin(list_of_users)]
    number_of_elements = len(df) if (len(df) < number_of_exported_elements) \
        else number_of_exported_elements
    df = df.sample(number_of_elements, random_state=42)

    # export sampled data and matching business
    df.to_json(
        output_file,
        orient="records",
        date_format="iso"
    )
    reviews_ids = list(df["review_id"].values)
    business_ids = list(df["business_id"].values)
    dates = list(df["date"].values)
    user_ids = list(df["user_id"].values)

    print(f"exported {len(df)} elements in {dataset_path}")
    return df, business_ids


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
    df = df.sample(number_of_elements, random_state=42)
    df.to_csv(output_file, index=False)
    print(f"exported {len(df)} elements in {dataset_path}")
    return df


def select_data(
        dataset_path,
        target_ids,
        target_column,
        number_of_elements=100
):
    input_file = os.path.join(DIR_DATA, dataset_path)
    output_file = os.path.join(DIR_DATA_TEST, dataset_path)
    os.makedirs(os.path.dirname(output_file), exist_ok=True)

    df = pd.read_json(input_file, lines=True, nrows=number_of_elements)
    df = df[df[target_column].isin(target_ids)]
    df.to_json(output_file, orient="records")

    print(f"exported {len(df)} elements in {dataset_path}")
    sampled_targed_elements = list(df[target_column].values)

    return df, sampled_targed_elements


def sample_random_json_data(dataset_path, number_of_elements=100):
    input_file = os.path.join(DIR_DATA, dataset_path)
    output_file = os.path.join(DIR_DATA_TEST, dataset_path)
    os.makedirs(os.path.dirname(output_file), exist_ok=True)
    df = pd.read_json(input_file, lines=True, nrows=number_of_elements)
    df.to_json(output_file, orient="records", date_format="iso")
    print(f"exported {len(df)} elements in {dataset_path}")
    return df


def sample_users_data(dataset_path, number_of_elements):
    df = sample_random_json_data(dataset_path, number_of_elements)
    sampled_users = list(df.user_id.values)
    return sampled_users


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

    # Sample users ( it is the biggest dataset )
    sampled_users = sample_users_data(datasets["users"],
                                      number_of_elements=1000)

    # Sample business reviewed by sampled users
    df_reviews, business_ids = sample_reviews(
        datasets["reviews"],
        list_of_users=sampled_users,
        number_of_loaded_elements=500000,
        number_of_exported_elements=1000
    )
    _, sampled_businesses = select_data(
        datasets["business_features"], business_ids, "business_id")

    # Sample dates
    df_extracted_dates = df_reviews[
        df_reviews["business_id"].isin(sampled_businesses)]
    dates = list(df_extracted_dates.date.values)
    _ = sample_weather_data(datasets["precipitations"], dates)
    _ = sample_weather_data(datasets["temperatures"], dates)

    # sample at random data excluded from star schema
    _ = sample_random_json_data(datasets["covid_features"])
    _ = sample_random_json_data(datasets["checkins"])
    _ = sample_random_json_data(datasets["tips"])


if __name__ == "__main__":
    main()
