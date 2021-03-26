from src import create_test_set, split_json_file
from src.constants import DIR_DATA_TEST


def main():
    create_test_set.main()

    split_json_file.main([
        f"--rel-path-file=yelp_dataset/yelp_academic_dataset_user.json",
        f"--base-dir={DIR_DATA_TEST}",
        "--chunk-size=2"
    ])

    split_json_file.main([
        f"--rel-path-file=yelp_dataset/yelp_academic_dataset_review.json",
        f"--base-dir={DIR_DATA_TEST}",
        "--chunk-size=2"
    ])


if __name__ == "__main__":
    main()
