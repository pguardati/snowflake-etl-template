import unittest

from src import split_dataset
from src.constants import DIR_DATA_TEST


class testSplit(unittest.TestCase):

    def test_split(self):
        split_dataset.main([
            f"--rel-path-file=yelp_dataset/yelp_academic_dataset_user.json",
            f"--base-dir={DIR_DATA_TEST}",
            "--chunk-size=2"
        ])
