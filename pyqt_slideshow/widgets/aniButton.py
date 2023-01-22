from PyQt5.QtCore import QPropertyAnimation, QAbstractAnimation
from PyQt5.QtWidgets import QAbstractButton


class AniAbstractButton(QAbstractButton):
    def __init__(self, size: int = 20):
        super().__init__()
        self.__initVal(size)
        self.__initUi()

    def __initVal(self, size):
        self.__size = size

    def __initUi(self):
        self.setFixedSize(self.__size, self.__size)
        self.__animation = QPropertyAnimation(self, b"border")
        self.__animation.valueChanged.connect(self._initStyle)
        self.__animation.setStartValue(0)
        max_border_width = self.__size//6
        self.__animation.setEndValue(max_border_width)
        self.__animation.setDuration(50)
        self._initStyle(self.__animation.startValue())

    def _getStyle(self, border_width):
        padding = abs(border_width-self.__animation.endValue())
        return f'''
            QAbstractButton 
            {{
            border: {border_width}px solid #AAAAAA;
            background-color: #CCCCCC;
            background-clip: content;
            padding: {padding};
            }}
            QAbstractButton:checked
            {{
            background-color: #888888;
            }}
            '''

    def _initStyle(self, border_width):
        self.setStyleSheet(self._getStyle(border_width))

    def enterEvent(self, e):
        self.__animation.setDirection(QAbstractAnimation.Forward)
        self.__animation.start()
        return super().enterEvent(e)

    def leaveEvent(self, e):
        self.__animation.setDirection(QAbstractAnimation.Backward)
        self.__animation.start()
        return super().leaveEvent(e)

    def event(self, e):
        if e.type() == 17:
            self._initStyle(self.__animation.startValue())
        return super().event(e)


class AniRadioButton(QRadioButton, AniAbstractButton):
    def __init__(self):
        super().__init__()

    def _initStyle(self, border_width):
        self.setStyleSheet(self._getStyle(border_width) + 'QRadioButton::indicator { border: none; }')