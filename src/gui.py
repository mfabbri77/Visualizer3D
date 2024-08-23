import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QVBoxLayout
from mpl_toolkits.mplot3d import Axes3D

class Visualizer3DWindow(QMainWindow):
    def __init__(self, x, y, z):
        super().__init__()
        self.x, self.y, self.z = x, y, z
        self.initUI()

    def initUI(self):
        self.setWindowTitle('3D Data Visualizer')
        self.setGeometry(100, 100, 800, 600)

        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)

        self.canvas = FigureCanvas(Figure(figsize=(5, 3)))
        layout.addWidget(self.canvas)

        self.ax = self.canvas.figure.add_subplot(111, projection='3d')
        self.scatter = self.ax.scatter(self.x, self.y, self.z)

        self.ax.set_xlabel('X')
        self.ax.set_ylabel('Y')
        self.ax.set_zlabel('Z')

        self.canvas.mpl_connect('button_press_event', self.on_click)
        self.canvas.mpl_connect('scroll_event', self.on_scroll)

    def on_click(self, event):
        if event.inaxes == self.ax:
            self.ax.mouse_init(rotate_btn=1, zoom_btn=3)

    def on_scroll(self, event):
        if event.inaxes == self.ax:
            factor = 0.95 if event.button == 'up' else 1.05
            self.ax.set_xlim3d(self.ax.get_xlim3d()[0] * factor, self.ax.get_xlim3d()[1] * factor)
            self.ax.set_ylim3d(self.ax.get_ylim3d()[0] * factor, self.ax.get_ylim3d()[1] * factor)
            self.ax.set_zlim3d(self.ax.get_zlim3d()[0] * factor, self.ax.get_zlim3d()[1] * factor)
            self.canvas.draw()

def run_gui(x, y, z):
    app = QApplication([])
    window = Visualizer3DWindow(x, y, z)
    window.show()
    app.exec_()
