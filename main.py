import sys
from MainWin import *
from Handler import *


if __name__ == '__main__':
    check = DatabaseLogic()

    app = QApplication(sys.argv)
    app.setStyleSheet(STYLE)
    main_window = UiMainWindow()
    main_window.setupUi()
    main_window.show()
    sys.exit(app.exec_())
