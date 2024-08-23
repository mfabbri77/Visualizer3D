# 3D Data Visualizer

This project is a Python-based 3D data visualization tool that allows users to visualize and interact with 3D data points from a text file.

## Features

- Load 3D data points from a text file
- Visualize data points in a 3D scatter plot
- Pan and zoom functionality using mouse controls
- Toggle surface visualization
- Command-line interface for specifying input file

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/3d-data-visualizer.git
   cd 3d-data-visualizer
   ```

2. Create a virtual environment (optional but recommended):
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

## Usage

Run the program from the command line, specifying the input file:

```
python main.py -i path/to/your/input_file.txt
```

The input file should have the following structure:

```
x=[x1, x2, x3, ...]
y=[y1, y2, y3, ...]
z=[z1, z2, z3, ...]
```

## Controls

- Left-click and drag: Rotate the view
- Right-click and drag: Pan the view
- Scroll wheel: Zoom in/out
- 'Toggle Surface' button: Switch between scatter plot and surface plot

## Running Tests

To run the tests, use the following command:

```
python -m pytest tests/
```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License.
