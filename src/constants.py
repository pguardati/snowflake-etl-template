import os

PROJECT_NAME = 'snowflake-etl-template'
REPOSITORY_PATH = os.path.realpath(__file__)[
                  :os.path.realpath(__file__).find(PROJECT_NAME)]
PROJECT_PATH = os.path.join(REPOSITORY_PATH, PROJECT_NAME)

DIR_DATA = os.path.join(os.path.expanduser("~"), "data", "snowflake_data")
DIR_DATA_TEST = os.path.join(PROJECT_PATH, "tests", "test_data")

# Test Database
DB_NAME = "test_snowflake"
DB_HOST = "localhost"
DB_USER = "postgres"
DB_PASSWORD = ""
DB_URI = f"postgresql://{DB_USER}@{DB_HOST}/{DB_NAME}"
