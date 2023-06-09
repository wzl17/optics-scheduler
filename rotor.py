from PyQt5.QtCore import Qt
from PyQt5.QtGui import QBrush, QPen, QPainter, QColor
from PyQt5.QtWidgets import QGraphicsItem, QGraphicsRectItem


class RotatingItem(QGraphicsRectItem):
    def __init__(self, x, y, w, h):
        super().__init__(x, y, w, h)
        self.setAcceptHoverEvents(True)
        self.setFlag(QGraphicsItem.ItemIsSelectable, True)
        self.setFlag(QGraphicsItem.ItemIsMovable, True)
        self.rotation_angle = 0
        self.hovered = False
        self.setTransformOriginPoint(w / 2, h / 2)
        self.setZValue(1)

    def paint(self, painter: QPainter, option, widget):
        rect = self.boundingRect()
        color = QColor(0, 255, 0)  # Green color
        if self.isSelected():
            color = QColor(255, 0, 0)  # Red color
        elif self.hovered:
            color = QColor(0, 0, 255)  # Blue color

        painter.setPen(QPen(Qt.black, 2))
        painter.setBrush(QBrush(color))
        painter.drawRect(rect)

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.rotate()

    def hoverEnterEvent(self, event):
        self.hovered = True
        self.update()

    def hoverLeaveEvent(self, event):
        self.hovered = False
        self.update()

    def rotate(self):
        self.rotation_angle += 90
        self.setRotation(self.rotation_angle)
        self.update()
