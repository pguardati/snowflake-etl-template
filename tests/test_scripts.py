import os
import warnings
import unittest
from subprocess import call

from etl_snowflake import stage_upload_data, db_execute_etls, \
    stage_dim_comparison
from src.constants import PROJECT_PATH, DIR_DATA_TEST

SNOWFLAKE_TEST_DB_NAME = "snowflake_test_db"
DIR_SCRIPTS = os.path.join(PROJECT_PATH, "etl_snowflake")


class TestModules(unittest.TestCase):
    def setUp(self):
        _ = call(
            f"snowsql -f {DIR_SCRIPTS}/db_reset.sql -D DB_NAME={SNOWFLAKE_TEST_DB_NAME}",
            shell=True
        )
        _ = call(
            f"snowsql -f {DIR_SCRIPTS}/stage_ddl.sql -d {SNOWFLAKE_TEST_DB_NAME}",
            shell=True
        )

    def test_upload_data(self):
        # suppress resource warning for snowflake requests in same session
        warnings.simplefilter("ignore", ResourceWarning)
        stage_upload_data.main([
            f"--db-name={SNOWFLAKE_TEST_DB_NAME}",
            f"--dir-data={DIR_DATA_TEST}"
        ])

    def test_dim_comparison(self):
        stage_dim_comparison.main([
            f"--db-name={SNOWFLAKE_TEST_DB_NAME}",
            f"--dir-data={DIR_DATA_TEST}"
        ])


class TestEtls(unittest.TestCase):
    def setUp(self):
        _ = call(
            f"snowsql -f {DIR_SCRIPTS}/db_reset.sql -D DB_NAME={SNOWFLAKE_TEST_DB_NAME}",
            shell=True
        )

    def test_etls(self):
        warnings.simplefilter("ignore", ResourceWarning)
        db_execute_etls.main([
            f"--db-name={SNOWFLAKE_TEST_DB_NAME}",
            f"--dir-data={DIR_DATA_TEST}",
            f"--dir-scripts={DIR_SCRIPTS}"
        ])