import os
import sys
import argparse
import pandas as pd


def partition_json_dataset(
        path_file,
        chunk_size=int(0.5 * 1e6)
):
    # create output directory
    dir_base = os.path.dirname(path_file)
    dataset_name = os.path.basename(path_file).split(".")[0] + "_partitioned"
    dir_output = os.path.join(dir_base, dataset_name)
    os.makedirs(dir_output, exist_ok=True)

    # read file, use a pointer
    chunks = pd.read_json(
        path_file,
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
        print(f"partition {partition_number} stored in {file_output}")
        df_chunk.to_json(
            file_output,
            orient="records",
            date_format="iso",
            lines=True
        )


def main(args=None):
    # parse command line arguments
    args = args or sys.argv[1:]
    parser = argparse.ArgumentParser()
    parser.add_argument("--rel-path-file")
    parser.add_argument("--base-dir")
    parser.add_argument("--chunk-size", type=int)
    args = parser.parse_args(args)
    # partition file
    path_file = os.path.join(args.base_dir, args.rel_path_file)
    partition_json_dataset(path_file, chunk_size=args.chunk_size)


if __name__ == "__main__":
    main()

