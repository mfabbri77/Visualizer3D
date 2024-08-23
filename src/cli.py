import argparse

def parse_arguments():
    parser = argparse.ArgumentParser(description="3D Data Visualizer")
    parser.add_argument("-i", "--input_file", required=True, help="Path to the input file containing x, y, z coordinates")
    return parser.parse_args()
