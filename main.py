#!/usr/bin/python3
# -*- coding: utf-8 -*-


'''
THE GUI
'''

import sys
from PyQt4.QtGui import QApplication, QWidget

if __name__ == '__main__':

    app = QApplication(sys.argv)

    w = QWidget()
    w.resize(250, 150)
    w.move(300, 300)
    w.setWindowTitle('test')
    w.show()

    sys.exit(app.exec_())
