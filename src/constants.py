import os
import configparser

PROJECT_NAME = 'snowflake-etl-template'
REPOSITORY_PATH = os.path.realpath(__file__)[
                  :os.path.realpath(__file__).find(PROJECT_NAME)]
PROJECT_PATH = os.path.join(REPOSITORY_PATH, PROJECT_NAME)

DIR_DATA = os.path.join(os.path.expanduser("~"), "data", "snowflake_data")

# Snowflake Database
DIR_CONFIG = os.path.join(PROJECT_PATH, "config")
snowflake_config_file = os.path.join(DIR_CONFIG, "snowflake.config")
snowflake_config = configparser.ConfigParser()
snowflake_config.read_file(open(snowflake_config_file))
SNOWFLAKE_USER = snowflake_config.get("SNOWFLAKE", "user")
SNOWFLAKE_PASSWORD = snowflake_config.get("SNOWFLAKE", "password")
SNOWFLAKE_ACCOUNT = snowflake_config.get("SNOWFLAKE", "account")
SNOWFLAKE_STAGING_JSON = "file_json"
SNOWFLAKE_STAGING_CSV = "file_csv"

# Test constants
# TODO: move in test directory
DIR_DATA_TEST = os.path.join(PROJECT_PATH, "tests", "test_data")

# Test Database
DB_NAME = "test_snowflake"
DB_HOST = "localhost"
DB_USER = "postgres"
DB_PASSWORD = ""
DB_URI = f"postgresql://{DB_USER}@{DB_HOST}/{DB_NAME}"
