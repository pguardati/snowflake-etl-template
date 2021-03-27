from unittest import TestCase

# TODO: add creation of test database and of staging

from etl_snowflake import stage_dim_comparison, stage_upload_data
from src.constants import DIR_DATA_TEST, SNOWFLAKE_TEST_DB_NAME


class TestScripts(TestCase):
    def test_dim_comparison(self):
        stage_dim_comparison.main([
            f"--db-name={SNOWFLAKE_TEST_DB_NAME}",
            f"--data-dir={DIR_DATA_TEST}"
        ])

    def test_upload_data(self):
        stage_upload_data.main([
            f"--db-name={SNOWFLAKE_TEST_DB_NAME}",
            f"--data-dir={DIR_DATA_TEST}"
        ])
