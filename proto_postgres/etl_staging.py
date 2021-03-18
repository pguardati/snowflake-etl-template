import psycopg2

from src.constants import DB_URI
from src.etl_prototype_pandas.read_staging import read_data
from proto_postgres import staging_cmd


def main():
    insert_queries = [
        staging_cmd.cmd_insert_precipitations,
        staging_cmd.cmd_insert_temperatures,
        staging_cmd.cmd_insert_covid_features,
        staging_cmd.cmd_insert_business,
        staging_cmd.cmd_insert_checkins,
        staging_cmd.cmd_insert_reviews,
        staging_cmd.cmd_insert_tips,
        staging_cmd.cmd_insert_users
    ]

    conn = psycopg2.connect(DB_URI)
    cur = conn.cursor()

    # reset tables
    cur.execute(staging_cmd.cmd_delete_tables)
    cur.execute(staging_cmd.cmd_create_tables)

    # extract and stage into the database
    df_list, table_names = read_data()
    for df, query in zip(df_list, insert_queries):
        for i, row in df.iterrows():
            cur.execute(query, row.astype(str).values)
    conn.close()
    print("Staging completed")


if __name__ == "__main__":
    main()
