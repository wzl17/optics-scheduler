from PyQt5.QtCore import Qt, QPointF
from PyQt5.QtWidgets import (
    QApplication,
    QGraphicsItem,
    QGraphicsPixmapItem,
    QGraphicsLineItem,
    QGraphicsSceneMouseEvent,
)
from PyQt5.QtGui import QPixmap


class Optics(QGraphicsPixmapItem):
    def __init__(self):
        super().__init__()
        self.setZValue(1)
        self.setFlag(QGraphicsItem.ItemIsMovable, True)
        self.setAcceptHoverEvents(True)

    def hoverEnterEvent(self, event) -> None:
        QApplication.setOverrideCursor(Qt.CursorShape.OpenHandCursor)

    def hoverLeaveEvent(self, event) -> None:
        QApplication.restoreOverrideCursor()

    # def mousePressEvent(self, event) -> None:
    #     QApplication.setOverrideCursor(Qt.CursorShape.ClosedHandCursor)

    # def mouseMoveEvent(self, event: QGraphicsSceneMouseEvent) -> None:
    #     old_cursor_pos = event.lastScreenPos()
    #     new_cursor_pos = event.screenPos()
    #     old_pos = self.scenePos()
    #     new_pos_x = new_cursor_pos.x() - old_cursor_pos.x() + old_pos.x()
    #     new_pos_y = new_cursor_pos.y() - old_cursor_pos.y() + old_pos.y()
    #     self.setPos(QPointF(new_pos_x, new_pos_y))

    # def mouseReleaseEvent(self, event) -> None:
    #     QApplication.restoreOverrideCursor()


class Coupler(Optics):
    def __init__(self):
        super().__init__()
        self.setPixmap(QPixmap("./figures/coupler.png"))
