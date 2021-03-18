def process_ods_reviews(df_reviews):
    # delete seconds from datetime - adapt to weather format
    df_reviews["date"] = df_reviews["date"].apply(
        lambda x: x.replace(hour=0, minute=0, second=0, microsecond=0))
    # select output columns
    columns = [
        'review_id',
        'date',
        'business_id',
        'user_id',
        'stars',
        'useful',
        'funny',
        'cool',
        'text'
    ]
    df_reviews = df_reviews[columns]
    df_reviews.sort_values(by=["date", "business_id", "user_id"], inplace=True)
    return df_reviews


def etl_ods_to_dwh(
        df_reviews,
        df_prec,
        df_temp,
        df_business_features,
        df_users
):
    # create dimension and fact tables
    df_fact_reviews = process_ods_reviews(df_reviews)
    df_dim_weather = df_prec.merge(df_temp, on="date")
    df_dim_business_features = df_business_features
    df_dim_users = df_users

    return df_fact_reviews, \
           df_dim_weather, \
           df_dim_business_features, \
           df_dim_users


def query_dwh(df_fact_reviews,
              df_dim_weather,
              df_dim_business_features,
              df_dim_users):
    df_query = df_fact_reviews.merge(
        df_dim_weather, on="date")
    df_query = df_query.merge(
        df_dim_business_features, on="business_id")
    df_query = df_query.merge(
        df_dim_users, on="user_id")
    return df_query
