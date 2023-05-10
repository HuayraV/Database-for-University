from PyQt5.QtCore import QRect, QSize
from PyQt5.QtWidgets import *
from settings import *
from DatabaseWin import *
import sqlite3 as sql


class UiMainWindow(QWidget):
    def __init__(self):
        super().__init__()
    
    def setupUi(self):
        ver = SETTINGS.get('Version')
        self.setWindowTitle(f'by WoollySensed Software | {ver}')
        self.resize(QSize(420, 260))
        self.setMinimumSize(QSize(420, 260))
        self.setMaximumSize(QSize(420, 260))
        self.setObjectName('Main_Window')

        self.btn_about = QPushButton(self)
        self.btn_about.setGeometry(QRect(370, 240, 50, 20))
        self.btn_about.setText('о нас')
        self.btn_about.setObjectName('About_Button')
        self.btn_about.clicked.connect(self.about_clicked)

        """CentralWidget"""
        self.centralWidget = QWidget(self)
        self.centralWidget.setGeometry(QRect(10, 10, 400, 200))
        self.centralWidget.setObjectName('Main_Window')

        self.led_firstname = QLineEdit(self.centralWidget)
        self.led_firstname.setGeometry(QRect(20, 0, 360, 30))
        self.led_firstname.setPlaceholderText('Введите имя')
        self.led_firstname.setMaxLength(50)
        self.led_firstname.setObjectName('Main_LineEdit')

        self.led_lastname = QLineEdit(self.centralWidget)
        self.led_lastname.setGeometry(QRect(20, 35, 360, 30))
        self.led_lastname.setPlaceholderText('Введите фамилию')
        self.led_lastname.setMaxLength(50)
        self.led_lastname.setObjectName('Main_LineEdit')

        self.led_direction = QLineEdit(self.centralWidget)
        self.led_direction.setGeometry(QRect(20, 70, 360, 30))
        self.led_direction.setPlaceholderText('Введите направление')
        self.led_direction.setMaxLength(50)
        self.led_direction.setObjectName('Main_LineEdit')

        self.led_course = QLineEdit(self.centralWidget)
        self.led_course.setGeometry(QRect(20, 105, 360, 30))
        self.led_course.setPlaceholderText('Введите курс')
        self.led_course.setMaxLength(50)
        self.led_course.setObjectName('Main_LineEdit')

        self.btn_del_student = QPushButton(self.centralWidget)
        self.btn_del_student.setGeometry(QRect(20, 140, 180, 25))
        self.btn_del_student.setText('УДАЛИТЬ СТУДЕНТА')
        self.btn_del_student.setObjectName('Main_Button')
        self.btn_del_student.clicked.connect(self.del_student_clicked)

        self.btn_add_student = QPushButton(self.centralWidget)
        self.btn_add_student.setGeometry(QRect(200, 140, 180, 25))
        self.btn_add_student.setText('ДОБАВИТЬ СТУДЕНТА')
        self.btn_add_student.setObjectName('Main_Button')
        self.btn_add_student.clicked.connect(self.add_student_clicked)

        self.btn_open_db = QPushButton(self.centralWidget)
        self.btn_open_db.setGeometry(QRect(20, 168, 360, 25))
        self.btn_open_db.setText('ОТКРЫТЬ БАЗУ ДАННЫХ')
        self.btn_open_db.setObjectName('Main_Button')
        self.btn_open_db.clicked.connect(self.open_databse_clicked)
        """/CentralWidget"""

    """Functions"""
    def about_clicked(self):
        QMessageBox.about(self, 'О НАС', SETTINGS.get('About_msg'))

    def open_databse_clicked(self):
        self.database = DatabaseWindow()
        self.database.setupUi()
        self.database.show()
    
    def add_student_clicked(self):
        #   Firstname
        self.input_fn = (self.led_firstname.text()).title()
        self.led_firstname.clear()
        #   Lastname
        self.input_ln = (self.led_lastname.text()).title()
        self.led_lastname.clear()
        #   Direction
        self.input_dir = (self.led_direction.text()).title()
        self.led_direction.clear()
        #   Course
        self.input_cr = self.led_course.text()
        self.led_course.clear()

        if all((self.input_fn, self.input_ln, self.input_dir, self.input_cr)):
            if self.input_cr in ('1', '2', '3', '4', '5'):
                with sql.connect(SETTINGS.get('Db_name')) as con:
                    cur = con.cursor()
                    cur.execute("""INSERT INTO students (firstname, lastname,
                    direction, course) VALUES (?, ?, ?, ?)""",
                    (self.input_fn, self.input_ln, self.input_dir, self.input_cr))
                    con.commit()
            else: QMessageBox.critical(self, 'Ошибка!', SETTINGS.get('Add_msg_2'))
        else: QMessageBox.information(self, 'Внимание!', SETTINGS.get('Add_msg_1'))
    
    def del_student_clicked(self):
        #   Firstname
        self.input_fn = (self.led_firstname.text()).title()
        self.led_firstname.clear()
        #   Lastname
        self.input_ln = (self.led_lastname.text()).title()
        self.led_lastname.clear()
        #   Direction
        self.input_dir = (self.led_direction.text()).title()
        self.led_direction.clear()
        #   Course
        self.input_cr = self.led_course.text()
        self.led_course.clear()

        if all((self.input_fn, self.input_ln, self.input_dir, self.input_cr)):
            if self.input_cr in ('1', '2', '3', '4', '5'):
                with sql.connect(SETTINGS.get('Db_name')) as con:
                    cur = con.cursor()
                    cur.execute(
                        """SELECT stud_id FROM students
                        WHERE (firstname=? AND lastname=? AND direction=? AND
                        course=?)""",
                        (self.input_fn, self.input_ln, self.input_dir, self.input_cr)
                    )
                    _id = cur.fetchone()
                    con.commit()

                    cur.execute("""DELETE FROM students WHERE (stud_id=?)""", (_id))
                    cur.execute("""DELETE FROM mod_subjects WHERE (mod_id=?)""", (_id))
                    con.commit()
                QMessageBox.information(self, 'Успех!', SETTINGS.get('Del_msg_1'))
            else: QMessageBox.critical(self, 'Ошибка!', SETTINGS.get('Add_msg_2'))
        else: QMessageBox.information(self, 'Внимание!', SETTINGS.get('Del_msg_2'))
    """/Functions"""
