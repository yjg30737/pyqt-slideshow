from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtGui import QPainter
from PyQt5.QtWidgets import QWidget, QGridLayout, QHBoxLayout, QButtonGroup, QSizePolicy
from pyqt_slideshow.widgets.aniButton import AniRadioButton
from pyqt_slideshow.widgets.graphicsView import SingleImageGraphicsView
from pyqt_slideshow.widgets.svgButton import SvgButton


class SlideShow(QWidget):
    def __init__(self):
        super().__init__()
        self.__initVal()
        self.__initUi()

    def __initVal(self):
        self.__btn = []
        self.__filenames = []
        self.__interval = 5000

    def __initUi(self):
        self.__view = SingleImageGraphicsView()
        self.__view.setAspectRatioMode(Qt.KeepAspectRatioByExpanding)
        self.__view.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.__view.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.__view.setStyleSheet('QGraphicsView { background: transparent; border: none; }')
        self.__view.installEventFilter(self)

        self.__btnGroup = QButtonGroup()
        self.__btnGroup.buttonClicked.connect(self.__showImageOfIdx)

        self.__btnWidget = QWidget()

        self.__prevBtn = SvgButton(self)
        self.__prevBtn.setIcon('ico/prev.svg')
        self.__prevBtn.setFixedSize(30, 50)
        self.__prevBtn.clicked.connect(self.__prev)
        self.__prevBtn.setEnabled(False)

        self.__nextBtn = SvgButton(self)
        self.__nextBtn.setIcon('ico/next.svg')
        self.__nextBtn.setFixedSize(30, 50)
        self.__nextBtn.clicked.connect(self.__nextClicked)

        lay = QHBoxLayout()
        lay.addWidget(self.__prevBtn, alignment=Qt.AlignLeft)
        lay.addWidget(self.__nextBtn, alignment=Qt.AlignRight)

        self.__navWidget = QWidget()
        self.__navWidget.setLayout(lay)

        lay = QGridLayout()
        lay.addWidget(self.__view, 0, 0, 3, 1)
        lay.addWidget(self.__navWidget, 0, 0, 3, 1)
        lay.addWidget(self.__btnWidget, 2, 0, 1, 1, Qt.AlignCenter)
        self.setLayout(lay)

        self.__timer = QTimer(self)
        self.__timer.setInterval(self.__interval)
        self.__timer.timeout.connect(self.__nextByTimer)
        self.__timer.start()

    def __showImageOfIdx(self, btn):
        idx = self.__btnGroup.id(btn)
        self.__view.setFilename(self.__filenames[idx])
        self.__prevNextBtnToggled(idx)
        self.__timer.start()

    def __prev(self):
        if len(self.__filenames) > 0:
            idx = max(0, self.__btnGroup.checkedId()-1)
            self.__updateViewAndBtnBasedOnIdx(idx)
            self.__timer.start()

    def __nextByTimer(self):
        if len(self.__filenames) > 0:
            self.__next()

    def __nextClicked(self):
        if len(self.__filenames) > 0:
            self.__next()
            self.__timer.start()

    def __next(self):
        idx = (self.__btnGroup.checkedId()+1) % len(self.__btnGroup.buttons())
        self.__updateViewAndBtnBasedOnIdx(idx)

    def __updateViewAndBtnBasedOnIdx(self, idx):
        self.__btnGroup.button(idx).setChecked(True)
        self.__view.setFilename(self.__filenames[idx])
        self.__prevNextBtnToggled(idx)

    def __prevNextBtnToggled(self, idx):
        self.__prevBtn.setEnabled(idx != 0)
        self.__nextBtn.setEnabled(idx != len(self.__btnGroup.buttons())-1)

    def setInterval(self, milliseconds: int):
        self.__timer.setInterval(milliseconds)

    def setFilenames(self, filenames: list):
        self.__filenames = filenames
        lay = QHBoxLayout()
        for i in range(len(self.__filenames)):
            btn = AniRadioButton()
            btn.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Minimum)
            lay.addWidget(btn)
            self.__btn.append(btn)
            self.__btnGroup.addButton(btn, i)
        self.__btn[0].setChecked(True)
        self.__view.setFilename(self.__filenames[0])
        self.__btnWidget.setLayout(lay)

    def setNavigationButtonVisible(self, f: bool):
        self.__navWidget.setVisible(f)

    def setBottomButtonVisible(self, f: bool):
        self.__btnWidget.setVisible(f)

    def setTimerEnabled(self, f: bool):
        if f:
            self.__timer.start()
        else:
            self.__timer.stop()

    def setGradientEnabled(self, f: bool):
        self.__view.setGradientEnabled(f)

    # to set the bottom buttons' size by user
    # here's how to do it:
    # for btn in self.__btnGroup.buttons():
    #     btn.setFixedSize(w, h)
    def getButtonGroup(self):
        return self.__btnGroup

    # get the btn widget
    # to set the spacing (currently)
    # here's how to do it:
    # self.__btnWidget.layout().setSpacing(5)
    def getBtnWidget(self):
        return self.__btnWidget

    # get the prev button
    # to set the prev nav button's size by user
    def getPrevBtn(self):
        return self.__prevBtn

    # get the next button
    # to set the next nav button's size by user
    def getNextBtn(self):
        return self.__nextBtn