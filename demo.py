import sys
from PyQt5.QtWidgets import QApplication, QGraphicsScene
from PyQt5.QtGui import QBrush, QPen
from PyQt5.QtCore import Qt
from pyqtgraph import GraphicsView, InfiniteLine, GridItem
from optics import Coupler


# class BeamPath(QGraphicsScene):
#     def __init__(self):
#         super.__init__()
#         self.lines = []

#     def paint(self):


class MainGraphicsView(GraphicsView):
    def __init__(self, parent=None, useOpenGL=None, background="w"):
        super().__init__(parent, useOpenGL, background)

        beam_origin = Coupler()
        beam_origin.setPos(75, 30)
        self.addItem(beam_origin)

        lines = [InfiniteLine(pos) for pos in range(0, 200, 50)] + [
            InfiniteLine(pos, angle=0) for pos in range(0, 200, 50)
        ]
        for line in lines:
            self.addItem(line)


app = QApplication(sys.argv)

graphicsView = MainGraphicsView(useOpenGL=True)
graphicsView.show()
app.exec_()
