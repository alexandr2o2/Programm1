from PyQt5.QtWidgets import QSizePolicy
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanavas


class MyMplCanvas(FigureCanavas):
    def __init__(self, fig, parent=None):
        super.__init__(self, self.fig)
        self.fig = fig
        FigureCanavas.setSizePolicy(self, QSizePolicy.Expanding, QSizePolicy.Expanding)
        FigureCanavas.updateGeometry(self)
