

from PyQt5 import QtGui, QtWidgets
from PyQt5.QtCore import QPointF
from PyQt5.QtGui import QPainter, QRadialGradient, QColor

from qtpy.QtWidgets import QApplication, QGraphicsScene
from pyqt_slideshow import SlideShow


# class MyGraphicsView(QtWidgets.QGraphicsView):
#     def __init__(self):
#         super().__init__()
#         scene = QGraphicsScene()
#         self.setScene(scene)
#
#         self.setStyleSheet(
#             '''
#             background-color: qradialgradient(spread: pad, cx: 0.5, cy: 0.5, radius: 1, fx: 0.5, fy: 0.5, stop: 0
#             rgba(255, 255, 255, 255), stop: 1
#             rgba(0, 0, 0, 150));
#             '''
#         )

if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)

    # # Create the QGraphicsView
    # graphics_view = MyGraphicsView()
    #
    # # Show the QGraphicsView
    # graphics_view.show()
    s = SlideShow()
    s.setFilenames(['a.png', 'b.png', 'c.png', 'd.png'])
    s.setGradientEnabled(True)
    for btn in s.getButtonGroup().buttons():
        btn.setFixedSize(40, 20)
    prevBtn = s.getPrevBtn()
    prevBtn.setFixedSize(60, 50)
    nextBtn = s.getNextBtn()
    nextBtn.setFixedSize(60, 50)
    s.show()
    app.exec_()