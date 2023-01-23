# pyqt-slideshow
PyQt widget for slide show

## Requirements
* PyQt5 >= 5.8

## Setup
`python -m pip install pyqt-slideshow`

## Detailed Description

![image](https://user-images.githubusercontent.com/55078043/170638847-1816f292-f731-49bc-bbb3-d7180e7ec779.png)

This widget mainly consists of three child widget.

* View
* Navigation button widget - buttons on the both sides of the view
* Bottom button widget - buttons at the bottom

You can set the image files to show with `setFilenames`.

You can watch previous/next image by clicking the navigation button or nth image file by clicking the buttons at the bottom.

Image is automatically changed by internal timer(QTimer). Interval is set to 5000 milliseconds by default.

## Method Overview
* `setFilenames(filenames: list)` - give the image files. You have to call this one time only so far.
* `setTimerEnabled(f: bool)` - set the image change timer
* `setInterval(milliseconds: int)` - set the image change interval
* `setNavigationButtonVisible(f: bool)` - set the navigation button's visibility(which also decides that you use it or not)
* `setBottomButtonVisible(f: bool)` - set the bottom button's visibility(which also decides that you use it or not)
* `setGradientEnabled(f: bool)` - Cover the dark gradient over the image

For example

<img src="https://user-images.githubusercontent.com/55078043/213953541-bc00a0c8-f11b-4054-8efe-7bdfead13262.png" width=320, height=200/>

* `getButtonGroup()` - get the button group(QButtonGroup) which has the every button. You can get them by `btnGrp.buttons()`
* `getBtnWidget()` - get the btn widget to set the spacing between the bottom button or other customization of button widget
* `getPrevBtn()` - get the prev button
* `getNextBtn()` - get the next button

## Example
### Code Sample 1 (Including navigation/bottom button)
```python
from PyQt5.QtWidgets import QApplication
from pyqt_slideshow import SlideShow

if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    s = SlideShow()
    s.setFilenames(['bioshock.jpg', 'dragon_age.jpg', 'ride_to_hell_retribution.jpg'])
    s.show()
    app.exec_()
```

### Result

https://user-images.githubusercontent.com/55078043/170615616-932fb93d-3311-4f97-8ad7-10943e0d2308.mp4

### Code Sample 2 (Not including navigation/bottom button)
```python
from PyQt5.QtWidgets import QApplication
from pyqt_slideshow import SlideShow

if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    s = SlideShow()
    s.setFilenames(['bioshock.jpg', 'dragon_age.jpg', 'ride_to_hell_retribution.jpg'])
    s.setNavigationButtonVisible(False) # to not show the navigation button
    s.setBottomButtonVisible(False) # to not show the bottom button
    s.show()
    app.exec_()
```

### Result

https://user-images.githubusercontent.com/55078043/170641896-336308b5-6f5c-4099-8b03-029a1f81337e.mp4

## TODO list
* Give the option to go back to first page by user when pressing the next button in the last page
* Transition effect
* Default screen when there is no image (thumbnail?)
* Add more styles with QML
