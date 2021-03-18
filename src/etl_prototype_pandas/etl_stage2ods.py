import pandas as pd


def rename_columns(df):
    raw_columns = df.columns
    processed_columns = []
    for col in raw_columns:
        processed_col = "_".join(col.lower().split())
        processed_columns.append(processed_col)
    for column_old, column_new in zip(raw_columns, processed_columns):
        df = df.rename(
            columns={column_old: column_new}
        )
    return df


def process_weather_dataset(df):
    # convert string to datetime format
    df["date"] = df.date.astype(str).str[:4] + "-" + \
                 df.date.astype(str).str[4:6] + "-" + \
                 df.date.astype(str).str[6:8]
    df["date"] = pd.to_datetime(df["date"])
    return df


def process_business_covid_dataset(df_business_covid):
    # TODO explode fields
    df_business_covid = df_business_covid.drop(
        ["highlights", "Covid Banner"], axis=1)
    df_business_covid = rename_columns(df_business_covid)
    return df_business_covid


def process_business_features_dataset(df_business_features):
    # TODO explode fields
    df_business_features = df_business_features.drop(
        ["attributes", "categories", "hours"], axis=1)
    return df_business_features


def process_checkin_features(df_checkins):
    # TODO: explode dates
    return df_checkins.drop(["date"], axis=1)


def process_users(df_users):
    # TODO: explode fields
    df_users = df_users.drop(["elite", "friends"], axis=1)
    return df_users


def etl_stage_to_ods(df_list):
    # weather data (pure copy)
    df_prec = process_weather_dataset(df_list[0])
    df_temp = process_weather_dataset(df_list[1])
    # yelp data (remove nested fields)
    df_business_covid = process_business_covid_dataset(df_list[2])
    df_business_features = process_business_features_dataset(df_list[3])
    df_checkins = process_checkin_features(df_list[4])
    df_reviews = df_list[5]
    df_tips = df_list[6]
    df_users = process_users(df_list[7])
    return df_prec, \
           df_temp, \
           df_business_covid, \
           df_business_features, \
           df_checkins, \
           df_reviews, \
           df_tips, \
           df_users


