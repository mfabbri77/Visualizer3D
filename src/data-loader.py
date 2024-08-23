import numpy as np

def load_data(file_path):
    with open(file_path, 'r') as f:
        content = f.read()

    x = np.array(eval(content.split('x=')[1].split('\n')[0]))
    y = np.array(eval(content.split('y=')[1].split('\n')[0]))
    z = np.array(eval(content.split('z=')[1].split('\n')[0]))

    return x, y, z
