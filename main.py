from PyQt5.QtWidgets import QApplication
from gui.windows.main import MainWindow
from src.core.objects.base import BaseObject
import sys
import subprocess
import os
import logging
import random


LOGGING_FORMAT = '%(levelname)s %(asctime)-15s Module %(module)s %(message)s'


def check_platform():
    if sys.platform.startswith("linux"):
        return "scripts/ui_convert.sh"
    elif sys.platform.startswith("win32"):
        return "scripts/ui_converter.bat"
    return "scripts/ui_convert.sh"


def ui_convert():
    path = os.getcwd()
    converter = check_platform()
    args = [converter, "static/ui", "gui/ui_generated"]
    subprocess.call([os.path.join(path, arg) for arg in args])


def main():
    random.seed()
    logging.basicConfig(format=LOGGING_FORMAT)
    BaseObject.logger = logging.getLogger('core')
    os.chdir(os.path.dirname(__file__))
    ui_convert()
    app = QApplication([])
    windows = MainWindow()
    windows.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
