from proto.config import read_data


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


def process_business_covid_dataset(df_business_covid):
    blacklisted_columns = ["highlights", "Covid Banner"]
    filtered_columns = list(filter(
        lambda column: column not in blacklisted_columns,
        list(df_business_covid.columns)
    ))
    df_business_covid = df_business_covid[filtered_columns]

    df_business_covid = rename_columns(df_business_covid)
    return df_business_covid


def process_business_features_dataset(df_business_features):
    blacklisted_columns = ["attributes", "categories", "hours"]
    filtered_columns = list(filter(
        lambda column: column not in blacklisted_columns,
        list(df_business_features.columns)
    ))
    df_business_features = df_business_features[filtered_columns]

    df_business_features = rename_columns(df_business_features)
    return df_business_features


df_list = read_data()

# weather data (pure copy)
df_prec = df_list[0]
df_temp = df_list[1]

# yelp data (remove nested fields)
df_business_covid = process_business_covid_dataset(df_list[2])
df_business_features = process_business_features_dataset(df_list[3])