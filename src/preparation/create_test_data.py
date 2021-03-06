from src.preparation import sample_datasets, split_json_file
from src.constants import DIR_DATA_TEST


def main():
    sample_datasets.main()

    split_json_file.main([
        f"--rel-path-file=yelp_dataset/yelp_academic_dataset_user.json",
        f"--base-dir={DIR_DATA_TEST}",
        "--chunk-size=5"
    ])

    split_json_file.main([
        f"--rel-path-file=yelp_dataset/yelp_academic_dataset_review.json",
        f"--base-dir={DIR_DATA_TEST}",
        "--chunk-size=5"
    ])


if __name__ == "__main__":
    main()
