#!/usr/bin/env python3
import sys
from src.cli import parse_arguments
from src.data_loader import load_data
from src.visualizer import visualize_data

def main():
    args = parse_arguments()
    x, y, z = load_data(args.input_file)
    visualize_data(x, y, z)

if __name__ == "__main__":
    main()
