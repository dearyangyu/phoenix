# !/usr/bin/python
# -*- coding :utf-8 -*-
"""
    Author: 白衬衣
    Data  : 2021/7/9
    Email : yangyuya2019@gmail.com
"""
# 测试
from PySide2 import QtWidgets, QtCore, QtGui

class DesktopWidget(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(DesktopWidget, self).__init__(parent)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    windows = DesktopWidget()
    windows.show()
    sys.exit(app.exec_())