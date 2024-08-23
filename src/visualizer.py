import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.widgets import Button

def visualize_data(x, y, z):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    scatter = ax.scatter(x, y, z)
    
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')

    def toggle_surface(event):
        if len(ax.collections) > 1:
            ax.collections[1].remove()
        else:
            ax.plot_trisurf(x, y, z, cmap='viridis', edgecolor='none', alpha=0.7)
        fig.canvas.draw()

    ax_button = plt.axes([0.81, 0.05, 0.1, 0.075])
    btn_surface = Button(ax_button, 'Toggle Surface')
    btn_surface.on_clicked(toggle_surface)

    plt.show()
