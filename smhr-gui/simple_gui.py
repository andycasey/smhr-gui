from PySide2.QtWidgets import *
from PySide2.QtCore import *
from PySide2.QtGui import *

import numpy as np
import sys

from test_ui import Ui_MainWindow

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)
        self.setWindowTitle("SMHR")

        ## Initialize state
        self.count = 0

        ## Connect menu options

        ## Connect buttons
        self.btn_dec.clicked.connect(lambda x: self.set_count(self.count-1))
        self.btn_inc.clicked.connect(lambda x: self.set_count(self.count+1))
        self.btn_toggle.clicked.connect(self.toggle_label)

        self.ax = self.mplplot.figure.add_subplot(111)
        self.ax.plot(np.arange(5), np.arange(5)+1, 'o-')
        self.mplplot.enable_interactive_zoom()
        self.mplplot.enable_drag_to_mask(self.ax)

    def set_count(self, number):
        print("Setting count")
        self.count = number
        self.label_count.setText(f"Count: {number}")
    def toggle_label(self, *args):
        print(*args)
        msg = self.label_msg.text()
        if msg == "Hello":
            self.label_msg.setText("Goodbye")
        else:
            self.label_msg.setText("Hello")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setApplicationName("SMHR")
    window = MainWindow()

    window.show()
    app.exec_()

