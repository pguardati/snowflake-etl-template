from src.etl_prototype_pandas.read_staging import read_data
from src.etl_prototype_pandas.etl_stage2ods import etl_stage_to_ods
from src.etl_prototype_pandas.etl_ods2dwh import etl_ods_to_dwh, query_dwh


def main():
    df_list = read_data()

    df_prec, df_temp, _, \
    df_business_features, _, \
    df_reviews, _, \
    df_users = etl_stage_to_ods(df_list)

    df_fact_reviews, \
    df_dim_weather, \
    df_dim_business_features, \
    df_dim_users = etl_ods_to_dwh(
        df_reviews,
        df_prec,
        df_temp,
        df_business_features,
        df_users
    )

    # query
    df_query = query_dwh(
        df_fact_reviews,
        df_dim_weather,
        df_dim_business_features,
        df_dim_users
    )


if __name__ == "__main__":
    main()
