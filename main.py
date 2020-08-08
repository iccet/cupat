from PyQt5.QtWidgets import QApplication
from gui.windows.main import MainWindow
import sys
import subprocess
import os


def ui_convert():
    path = os.getcwd()
    args = ["scripts/ui_convert.sh", "static/ui", "gui/ui_generated"]
    subprocess.call([os.path.join(path, arg) for arg in args])


def main():
    os.chdir(os.path.dirname(__file__))
    ui_convert()
    app = QApplication([])
    windows = MainWindow()
    windows.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
