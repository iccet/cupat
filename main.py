from PyQt5.QtWidgets import QApplication
from src.gui.windows.main import MainWindow
import sys
import subprocess


def main():
    subprocess.call("./ui_convert.sh")
    app = QApplication([])
    windows = MainWindow()
    windows.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
