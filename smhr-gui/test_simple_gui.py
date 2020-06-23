from simple_gui import MainWindow
from PySide2 import QtCore, QtGui
from PySide2.QtWidgets import QApplication, QDialog, QLabel, QVBoxLayout


def test_count_increment(qtbot):
    widget = MainWindow()
    qtbot.addWidget(widget)

    qtbot.mouseClick(widget.btn_inc, QtCore.Qt.LeftButton)

    assert widget.count == 1
    assert widget.label_count.text() == "Count: 1"


def test_button_toggle(qtbot):
    widget = MainWindow()
    qtbot.addWidget(widget)

    for i in range(10):

        qtbot.mouseClick(widget.btn_toggle, QtCore.Qt.LeftButton)

        expected = ["Goodbye", "Hello"][i % 2]
        assert widget.label_msg.text() == expected

    
def test_count_decrement(qtbot):
    widget = MainWindow()
    qtbot.addWidget(widget)

    up, down = (5, 3)
    for i in range(up):
        qtbot.mouseClick(widget.btn_inc, QtCore.Qt.LeftButton)

    assert widget.label_count.text() == f"Count: {up}"

    for j in range(down):
        qtbot.mouseClick(widget.btn_dec, QtCore.Qt.LeftButton)
    
    assert widget.count == (up - down)
    assert widget.label_count.text() == f"Count: {up - down}"




def test_drag_to_mask(qtbot):
    
    widget = MainWindow()
    qtbot.addWidget(widget)

    for ax, masks in widget.mplplot._masked_regions.items():
        assert len(masks) == 0


    start_pos, end_pos = QtCore.QPoint(300, 500), QtCore.QPoint(400, 300)

    def on_value_changed(value):
        event = QtGui.QMouseEvent(
            QtCore.QEvent.MouseMove,
            value,
            QtCore.Qt.NoButton,
            QtCore.Qt.LeftButton,
            QtCore.Qt.NoModifier,
        )
        QtCore.QCoreApplication.sendEvent(widget.mplplot, event)

    animation = QtCore.QVariantAnimation(
        startValue=start_pos, endValue=end_pos, duration=1000
    )

    qtbot.mousePress(widget.mplplot, QtCore.Qt.LeftButton)
    animation.valueChanged.connect(on_value_changed)
    with qtbot.waitSignal(animation.finished, timeout=10000):
        animation.start()
    qtbot.mouseRelease(widget.mplplot, QtCore.Qt.LeftButton)

    # Check that we made a mask region visible.
    for ax, masks in widget.mplplot._masked_regions.items():
        assert len(masks) == 1

