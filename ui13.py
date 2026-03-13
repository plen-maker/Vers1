# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets
import subprocess
import sys
import os

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1143, 549)
        Form.setStyleSheet("background-color:qlineargradient(spread:pad, x1:0.398, y1:0.357955, x2:1, y2:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(81, 81, 81, 255))")
        
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(400, 230, 331, 91))
        self.pushButton.setStyleSheet("background-color: rgb(255, 255, 255); font-size: 14pt; font-weight: bold;")
        self.pushButton.setObjectName("pushButton")
        
        self.textBrowser = QtWidgets.QTextBrowser(Form)
        self.textBrowser.setGeometry(QtCore.QRect(480, 20, 161, 71))
        self.textBrowser.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.textBrowser.setObjectName("textBrowser")
        
        self.textEdit = QtWidgets.QTextEdit(Form)
        self.textEdit.setGeometry(QtCore.QRect(10, 490, 421, 31))
        self.textEdit.setStyleSheet("background: transparent; border: none;")
        self.textEdit.setObjectName("textEdit")
        self.textEdit.setReadOnly(True)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

        # GOMB ÖSSZEKÖTÉSE
        self.pushButton.clicked.connect(self.launch_game)

    def launch_game(self):
        """Ez a függvény megkeresi az xairos.py-t a TEMP mappában és elindítja"""
        
        # 1. Lekérjük a Windows TEMP mappa elérési útját
        temp_path = os.environ.get('TEMP')
        target_file = "xairos.py"
        
        # 2. Összerakjuk a teljes útvonalat (pl. C:\Users\Név\AppData\Local\Temp\xairos.py)
        full_path = os.path.join(temp_path, target_file)
        
        # Debug: kiírjuk a konzolra, hogy pontosan hol keressük (segít a hibakeresésben)
        print(f"Keresés itt: {full_path}")

        if os.path.exists(full_path):
            try:
                # Elindítás a Python-nal
                subprocess.Popen([sys.executable, full_path])
                # Az indító ablak bezárása
                QtWidgets.QApplication.instance().activeWindow().close()
            except Exception as e:
                QtWidgets.QMessageBox.critical(None, "Hiba", f"Nem sikerült elindítani: {e}")
        else:
            # Ha nem találja a fájlt a Temp-ben
            msg = QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Warning)
            msg.setWindowTitle("Hiányzó fájl")
            msg.setText("A játékfájl nem található!")
            msg.setInformativeText(f"Az xairos.py nincs a Temp mappában.\n\nÚtvonal: {full_path}")
            msg.exec_()

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Xairos Launcher"))
        self.pushButton.setText(_translate("Form", "Play the real game!"))
        self.textBrowser.setHtml(_translate("Form", "<html><body><p align='center'><span style='font-size:36pt;'>XairOs</span></p></body></html>"))
        self.textEdit.setHtml(_translate("Form", "<html><body><p><span style='color:#ffffff;'>If something not working pls contact me on discord: ddnemet</span></p></body></html>"))

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())