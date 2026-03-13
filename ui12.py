from PyQt5 import QtCore, QtGui, QtWidgets
import subprocess # Ez kell a fájl megnyitásához
import sys
import os

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1430, 947)
        Form.setAutoFillBackground(False)
        Form.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0.443182 rgba(0, 0, 0, 255), stop:0.448864 rgba(255, 184, 103, 255), stop:0.505682 rgba(33, 123, 131, 255), stop:0.517045 rgba(159, 121, 255, 255), stop:0.539773 rgba(207, 83, 255, 255), stop:0.642045 rgba(10, 26, 255, 255));")
        
        self.textBrowser = QtWidgets.QTextBrowser(Form)
        self.textBrowser.setGeometry(QtCore.QRect(500, 60, 351, 71))
        self.textBrowser.setStyleSheet("background-color: rgb(211, 211, 211);")
        self.textBrowser.setObjectName("textBrowser")
        
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(50, 830, 351, 71))
        self.pushButton.setStyleSheet("color: rgb(0, 0, 0); background-color: white;")
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(Form)
        
        # --- ÖSSZEKÖTÉS ---
        # Amikor rákattintasz a Continue gombra, lefut a 'megnyitas' függvény
        self.pushButton.clicked.connect(self.megnyitas)

    def megnyitas(self):
        # Megkeressük az xairos.py-t abban a mappában, ahol ez a fájl is van
        fajl_neve = "xairos.py"
        
        if os.path.exists(fajl_neve):
            # Elindítjuk a Python segítségével az xairos.py-t egy új ablakban
            subprocess.Popen([sys.executable, fajl_neve])
            # Ha azt akarod, hogy a Welcome ablak bezáródjon a megnyitás után, add hozzá ezt:
            # Form.close() 
        else:
            # Ha nem találja a fájlt, feldob egy hibaüzenetet
            error_msg = QtWidgets.QMessageBox()
            error_msg.setText(f"Hiba: A(z) {fajl_neve} nem található a mappában!")
            error_msg.exec_()

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Xos"))
        self.textBrowser.setHtml(_translate("Form", "<html><body><p align='center'><span style='font-size:36pt; color:#000000;'>Welcome to Xos</span></p></body></html>"))
        self.pushButton.setText(_translate("Form", "Continue"))

# Az import re_rc-t kivettem, mert az okozta a hibát

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())