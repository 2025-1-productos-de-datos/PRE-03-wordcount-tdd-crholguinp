import sys
import argparse

def parse_args():

    parser = argparse.ArgumentParser(description="Count words in text files.")

    parser.add_argument(
        "input", type=str, 
        help="Path to the input folder containing text files.",
    )
    parser.add_argument(
        "output", 
        type=str, 
        help="Path to the output folder for results.",
    )

    parsed_args = parser.parse_args()

    return parsed_args.input, parsed_args.output