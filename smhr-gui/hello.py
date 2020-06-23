from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import Slot


class HelloWidget(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(HelloWidget, self).__init__(parent)

        self.button_greet = QtWidgets.QPushButton()
        self.greet_label = QtWidgets.QLabel()
        self.button_greet.clicked.connect(self.set_text)

    def set_text(self):
        self.greet_label.setText('Hello!')

'''
def test_hello(qtbot):
    widget = HelloWidget()
    qtbot.addWidget(widget)

    # click in the Greet button and make sure it updates the appropriate label
    qtbot.mouseClick(widget.button_greet, QtCore.Qt.LeftButton)

    assert widget.greet_label.text() == 'Hello!'
'''
