"""
    # Copyright © 2023 By Nguyễn Phú Khương
    # ZALO : 0363561629
    # Email : dev.phukhuong0709@hotmail.com
    # Github : npk-0709
"""

from PyQt5 import QtCore

class CoreThreadUpdate(QtCore.QThread):
    signals = QtCore.pyqtSignal(list)

    def __init__(self,data):
        super().__init__()
        self.data = data
        
    def run(self):
        self.signals.emit(self.data)

class ThreadUpdate:
    def __init__(self,data):
        self.threads = CoreThreadUpdate(data)
        self.threads.signals.connect(data[1])
        
    def update(self):
        self.threads.start()
        self.threads.wait()
        self.threads.exit()