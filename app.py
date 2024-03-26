"""
    # Copyright © 2022 By Nguyễn Phú Khương
    # ZALO : 0363561629
    # Email : dev.phukhuong0709@hotmail.com
    # Github : npk-0709
"""
from ui import *
import sys
import os
import threading
from PyQt5.QtWidgets import QFileDialog
import numpy
from coreThread import *
import ctypes
from func import *




class core(Ui_MainWindow, QtWidgets.QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.setupUi(self)
        self.total.setStyleSheet(f"color: blue;font-weight: bold;")
        self.die.setStyleSheet(f"color: red;font-weight: bold;")
        self.live.setStyleSheet(f"color: green;font-weight: bold;")
        self.btnEvent.setStyleSheet(f"color: green;font-weight: bold;")
        self.btnEvent.clicked.connect(lambda: threading.Thread(target=self._btnEvents).start())
        self.btnOpenFile.clicked.connect(lambda: self.openFile())
        self.btnExportFileDie.clicked.connect(lambda: self.exportFile(False))
        self.btnExportFileLive.clicked.connect(lambda: self.exportFile(True))
    
    def openFile(self):
        try:
            path_file = QFileDialog.getOpenFileNames()[0][0]
            with open(path_file,'r',encoding='utf-8') as f:
                self.dataAll.appendPlainText(f.read())
            ThreadUpdate([None,self.callback_updatedata]).update()
        except:pass


    def _btnEvents(self):
        if self.isUid.isChecked() == False and self.isCookie.isChecked() == False and self.isToken.isChecked() == False:
            ctypes.windll.user32.MessageBoxW(0, f"VUI LÒNG CHỌN KIỂU CHẠY Ở MỤC TRÊN ", "NOTIFICATION", 64)
            return
        if self.btnEvent.text() == "CHECK LIVE":
            self.isRunning = True
            self.btnEvent.setStyleSheet(f"color: red;font-weight: bold;")
            self.btnEvent.setText("CLICK TO STOP")
            datas = list(numpy.array_split(self.dataAll.toPlainText().split('\n'),self.numThread.value()))
            for data in datas:
                threading.Thread(target=self.appmain,args=(data,)).start()


        else:
            self.btnEvent.setStyleSheet(f"color: green;font-weight: bold;")
            self.btnEvent.setText("CHECK LIVE")
            self.isRunning = False
    
    def exportFile(self,live=True):
        
        try:
            if live:
                with open('result.live.txt','a+',encoding='utf-8') as f:
                    f.write(self.dataLive.toPlainText())
                ctypes.windll.user32.MessageBoxW(0, "XUẤT FILE THÀNH CÔNG `result.live.txt`", "EXPORT SUCCESS", 64)
            else:
                with open('result.die.txt','a+',encoding='utf-8') as f:
                    f.write(self.dataDie.toPlainText())
                ctypes.windll.user32.MessageBoxW(0, "XUẤT FILE THÀNH CÔNG `result.die.txt`", "EXPORT SUCCESS", 64)
        except Exception as e:
            ctypes.windll.user32.MessageBoxW(0, f"XUẤT FILE THẤT BẠI `{str(e)}`", "EXPORT ERROR", 64)
        
    
    def appmain(self,data:list):
        for datax in data:
            if self.isRunning == False:
                break
            if self.isUid.isChecked():
                result = APP().checkLiveUid(str(datax).strip())
                if result == True:
                    ThreadUpdate([[self.dataLive,datax],self.callback_result]).update()
                if result == False:
                    ThreadUpdate([[self.dataDie,datax],self.callback_result]).update()
                if result == None:
                    ThreadUpdate([[self.dataDie,datax],self.callback_result]).update()

            elif self.isCookie.isChecked():
                result = APP().checkLiveCookie(str(datax).strip())
                if result == True:
                    ThreadUpdate([[self.dataLive,datax],self.callback_result]).update()
                if result == False:
                    ThreadUpdate([[self.dataDie,datax],self.callback_result]).update()
                if result == None:
                    ThreadUpdate([[self.dataDie,datax],self.callback_result]).update()
            
            elif self.isToken.isChecked():
                result = APP().checkLiveToken(str(datax).strip())
                if result == True:
                    ThreadUpdate([[self.dataLive,datax],self.callback_result]).update()
                if result == False:
                    ThreadUpdate([[self.dataDie,datax],self.callback_result]).update()
                if result == None:
                    ThreadUpdate([[self.dataDie,datax],self.callback_result]).update()
            else:
                ctypes.windll.user32.MessageBoxW(0, f"VUI LÒNG CHỌN KIỂU CHẠY Ở MỤC TRÊN ", "NOTIFICATION", 64)
                self.btnEvent.setStyleSheet(f"color: green;font-weight: bold;")
                self.btnEvent.setText("CHECK LIVE")
                self.isRunning = False
                return
            ThreadUpdate([None,self.callback_updatedata]).update()
        








    def callback_updatedata(self, _):
        total = str(len(self.dataAll.toPlainText().split('\n')))
        die = str(len(self.dataDie.toPlainText().split('\n')))
        live = str(len(self.dataLive.toPlainText().split('\n')))
        if self.dataLive.toPlainText().strip() == '':
            live = '0'
        if self.dataDie.toPlainText().strip() == '':
            die = '0'
        self.total.setText(total)
        self.die.setText(die)
        self.live.setText(live)
    
    def callback_result(self,data:list):
        data[0][0].appendPlainText(data[0][1].strip())
        




app = QtWidgets.QApplication(sys.argv)
cores = core()
cores.show()
sys.exit(app.exec_())