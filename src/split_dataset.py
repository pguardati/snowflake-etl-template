import os
import pandas as pd
from src.constants import DIR_DATA_TEST, DIR_DATA


def partition_dataset(path_input):
    # create output directory
    dir_base = os.path.dirname(path_input)
    dataset_name = os.path.basename(path_input).split(".")[0] + "_partitioned"
    dir_output = os.path.join(dir_base, dataset_name)
    os.makedirs(dir_output, exist_ok=True)

    # read file, use a pointer
    chunks = pd.read_json(
        path_input,
        lines=True,
        chunksize=chunk_size
    )

    # read chunk and store it, iteratively
    for partition_number, df_chunk in enumerate(chunks):
        # create output file
        file_output = os.path.join(
            dir_output,
            f"{dataset_name}_{partition_number}.json"
        )
        # store partition
        print(f"partition {partition_number} stored id {file_output}")
        df_chunk.to_json(
            file_output,
            orient="records",
            date_format="iso",
            lines=True
        )


# partition_dataset(path_input)

chunk_size = int(0.5 * 1e6)
chunk_size = 2
path_input = os.path.join(
    DIR_DATA_TEST,
    "yelp_dataset/yelp_academic_dataset_user.json"
)

# todo: wrap as script, use into bigger files