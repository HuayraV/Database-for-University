from PyQt5.QtCore import QRect, QSize
from PyQt5.QtWidgets import *
from settings import *
import sqlite3 as sql


class DatabaseWindow(QWidget):
    def __init__(self):
        super().__init__()
    
    def setupUi(self):
        self.setWindowTitle('БАЗА ДАННЫХ СТУДЕНТОВ')
        self.resize(QSize(1000, 587))
        self.setMinimumSize(QSize(1000, 587))
        self.setObjectName('Db_Window')

        """CentralWidget"""
        self.centralWidget = QWidget(self)
        self.centralWidget.resize(QSize(720, 587))
        self.centralWidget.setObjectName('Db_Window')

        with sql.connect(SETTINGS.get('Db_name')) as con:
            cur = con.cursor()
            cur.execute(
                """SELECT firstname, lastname, direction, course
                FROM students"""
            )
            students = cur.fetchall()
            con.commit()
            cur.execute("""SELECT subject, score_lectures, score_seminars, 
                score_labs, score_practice FROM mod_subjects""")
            mod_subject = cur.fetchall()
            con.commit()
        
        names_list = [f'{names[0]} {names[1]}' for names in students]
        subjects_list = {subj[0] for subj in mod_subject}

        vbox = QVBoxLayout(self.centralWidget)
        
        #   Tab 1
        column_lbls = ['Имя', 'Фамилия', 'Направление', 'Курс']
        self.TableWidget = QTableWidget()
        self.TableWidget.setColumnCount(4)
        self.TableWidget.setHorizontalHeaderLabels(column_lbls)
        self.TableWidget.setSortingEnabled(True)

        #   Отображение стартовой таблицы
        count = 0
        for el in students:
            self.TableWidget.setRowCount(len(students))

            _fn = QTableWidgetItem(str(el[0]))
            _ln = QTableWidgetItem(str(el[1]))
            _dir = QTableWidgetItem(str(el[2]))
            _cr = QTableWidgetItem(str(el[3]))

            self.TableWidget.setItem(count, 0, _fn)
            self.TableWidget.setItem(count, 1, _ln)
            self.TableWidget.setItem(count, 2, _dir)
            self.TableWidget.setItem(count, 3, _cr)

            count += 1

        self.tab1_1 = QWidget()
        self.tab1_1.layout = QVBoxLayout()
        self.tab1_1.layout.addWidget(self.TableWidget)
        self.tab1_1.setLayout(self.tab1_1.layout)

        # Tab Parent
        self.tabs = QTabWidget()
        self.tabs.addTab(self.tab1_1, 'Все студенты')

        vbox.addWidget(self.tabs)
        """/CentralWidget"""

        """ControlPanel"""
        self.controlPanel = QWidget(self)
        self.controlPanel.setGeometry(QRect(720, 0, 280, 720))
        self.controlPanel.setObjectName('Db_Window')
        """Добавление баллов по предмету"""
        self.lbl_score = QLabel(self.controlPanel)
        self.lbl_score.setGeometry(QRect(0, 10, 271, 40))
        self.lbl_score.setText('Добавление баллов по предмету')
        self.lbl_score.setFrameShape(QFrame.Box)
        self.lbl_score.setObjectName('Db_Label')

        self.cb_subjs = QComboBox(self.controlPanel)
        self.cb_subjs.setGeometry(QRect(0, 50, 271, 30))
        self.cb_subjs.addItems(subjects_list)
        self.cb_subjs.setObjectName('Db_ComboBox')

        self.cb_names = QComboBox(self.controlPanel)
        self.cb_names.setGeometry(QRect(0, 80, 271, 30))
        self.cb_names.addItems(names_list)
        self.cb_names.setObjectName('Db_ComboBox')

        self.led_sc_lec = QLineEdit(self.controlPanel)
        self.led_sc_lec.setGeometry(QRect(0, 110, 271, 30))
        self.led_sc_lec.setPlaceholderText('Баллы за лекции')
        self.led_sc_lec.setMaxLength(4)
        self.led_sc_lec.setObjectName('Db_LineEdit')

        self.led_sc_sem = QLineEdit(self.controlPanel)
        self.led_sc_sem.setGeometry(QRect(0, 140, 271, 30))
        self.led_sc_sem.setPlaceholderText('Баллы за семинары')
        self.led_sc_sem.setMaxLength(4)
        self.led_sc_sem.setObjectName('Db_LineEdit')

        self.led_sc_lab = QLineEdit(self.controlPanel)
        self.led_sc_lab.setGeometry(QRect(0, 170, 271, 30))
        self.led_sc_lab.setPlaceholderText('Баллы за лабораторные')
        self.led_sc_lab.setMaxLength(4)
        self.led_sc_lab.setObjectName('Db_LineEdit')

        self.led_sc_prac = QLineEdit(self.controlPanel)
        self.led_sc_prac.setGeometry(QRect(0, 200, 271, 30))
        self.led_sc_prac.setPlaceholderText('Баллы за практику')
        self.led_sc_prac.setMaxLength(4)
        self.led_sc_prac.setObjectName('Db_LineEdit')

        self.btn_accept = QPushButton(self.controlPanel)
        self.btn_accept.setGeometry(QRect(0, 231, 271, 20))
        self.btn_accept.setText('ДОБАВИТЬ БАЛЛЫ')
        self.btn_accept.setObjectName('Db_Button')
        self.btn_accept.clicked.connect(self.add_score_clicked)
        """/Добавление баллов по предмету"""

        """Добавление предмета студенту"""
        self.lbl_add_subject = QLabel(self.controlPanel)
        self.lbl_add_subject.setGeometry(QRect(0, 259, 271, 40))
        self.lbl_add_subject.setText('Выберите кому и какой\nпредмет добавить')
        self.lbl_add_subject.setFrameShape(QFrame.Box)
        self.lbl_add_subject.setObjectName('Db_Label')

        self.cb_names_3 = QComboBox(self.controlPanel)
        self.cb_names_3.setObjectName('Db_ComboBox')
        self.cb_names_3.setGeometry(QRect(0, 299, 271, 30))
        self.cb_names_3.addItems(names_list)

        self.led_subject = QLineEdit(self.controlPanel)
        self.led_subject.setGeometry(QRect(0, 329, 271, 30))
        self.led_subject.setPlaceholderText('Название предмета')
        self.led_subject.setMaxLength(50)  # redact
        self.led_subject.setObjectName('Db_LineEdit')

        self.btn_accept_2 = QPushButton(self.controlPanel)
        self.btn_accept_2.setGeometry(QRect(0, 360, 271, 20))
        self.btn_accept_2.setText('ДОБАВИТЬ ПРЕДМЕТ')
        self.btn_accept_2.setObjectName('Db_Button')
        self.btn_accept_2.clicked.connect(self.add_subject_clicked)
        """/Добавление предмета студенту"""

        """Успеваемость студента"""
        self.lbl_view_stud = QLabel(self.controlPanel)
        self.lbl_view_stud.setGeometry(QRect(0, 388, 271, 40))
        self.lbl_view_stud.setText('Выберите студента для\nпросмотра его успеваемости')
        self.lbl_view_stud.setFrameShape(QFrame.Box)
        self.lbl_view_stud.setObjectName('Db_Label')

        self.cb_names_2 = QComboBox(self.controlPanel)
        self.cb_names_2.setGeometry(QRect(0, 428, 271, 30))
        self.cb_names_2.addItems(names_list)
        self.cb_names_2.setObjectName('Db_ComboBox')

        self.btn_accept_3 = QPushButton(self.controlPanel)
        self.btn_accept_3.setGeometry(QRect(0, 459, 271, 20))
        self.btn_accept_3.setText('ВЫБРАТЬ СТУДЕНТА')
        self.btn_accept_3.setObjectName('Db_Button')
        self.btn_accept_3.clicked.connect(self.open_stud_info)
        """/Успеваемость студента"""
        
        """Успеваемость по предмету"""
        self.lbl_view_subjs = QLabel(self.controlPanel)
        self.lbl_view_subjs.setGeometry(QRect(0, 487, 271, 40))
        self.lbl_view_subjs.setText('Выберите предмет для\nпросмотра успеваемости по нему')
        self.lbl_view_subjs.setFrameShape(QFrame.Box)
        self.lbl_view_subjs.setObjectName('Db_Label')

        self.cb_subjs_2 = QComboBox(self.controlPanel)
        self.cb_subjs_2.setObjectName('Db_ComboBox')
        self.cb_subjs_2.setGeometry(QRect(0, 527, 271, 30))
        self.cb_subjs_2.addItems(subjects_list)

        self.btn_accept_4 = QPushButton(self.controlPanel)
        self.btn_accept_4.setGeometry(QRect(0, 558, 271, 20))
        self.btn_accept_4.setText('ВЫБРАТЬ ПРЕДМЕТ')
        self.btn_accept_4.setObjectName('Db_Button')
        self.btn_accept_4.clicked.connect(self.open_subj_info)
        """/Успеваемость по предмету"""
        
        """Дополнительная информация"""
        self.btn_info = QPushButton(self.controlPanel)
        self.btn_info.setGeometry(QRect(251, 10, 20, 20))
        self.btn_info.setText('?')
        self.btn_info.setObjectName('Db_Button_Info')
        self.btn_info.clicked.connect(self.info_clicked)
        """/Дополнительная информация"""
        """/ControlPanel"""
    
    """Functions"""
    """Открывает QMessageBox с информацией о разделе"""
    def info_clicked(self):
        QMessageBox.about(self,
            'Использование данного раздела',
            SETTINGS.get('Info_msg')
        )

    """Добавляет предмет в БД"""
    def add_subject_clicked(self):
        name = (self.cb_names_3.currentText()).split()
        subj = (self.led_subject.text()).title()
        self.led_subject.clear()

        if subj:
            with sql.connect(SETTINGS.get('Db_name')) as con:
                cur = con.cursor()
                cur.execute(
                    """SELECT stud_id FROM students WHERE firstname=?
                    AND lastname=?""",
                    (name[0], name[1])
                )
                _id = cur.fetchone()
                cur.execute("""INSERT INTO mod_subjects (mod_id, subject)
                VALUES (?, ?)""", (_id[0], subj))
                con.commit()
        else: QMessageBox.information(self, 'Внимание!', SETTINGS.get('Add_msg_3'))
    
    """Прибавляет, либо вычитает баллы по предмету"""
    def add_score_clicked(self):
        name = (self.cb_names.currentText()).split()
        subj = self.cb_subjs.currentText()
        lec = self.led_sc_lec.text()
        sem = self.led_sc_sem.text()
        lab = self.led_sc_lab.text()
        prac = self.led_sc_prac.text()
        
        self.led_sc_lec.clear()
        self.led_sc_sem.clear()
        self.led_sc_lab.clear()
        self.led_sc_prac.clear()
        
        if all((lec, sem, lab, prac)):
            with sql.connect(SETTINGS.get('Db_name')) as con:
                cur = con.cursor()
                cur.execute(
                    """SELECT stud_id FROM students
                    WHERE (firstname=? AND lastname=?)""",
                    (name[0], name[1])
                )
                _id = cur.fetchone()
                cur.execute(
                    """SELECT score_lectures, score_seminars, score_labs,
                    score_practice FROM mod_subjects
                    WHERE (mod_id=? AND subject=?)""",
                    (_id[0], subj)
                )
                _score = cur.fetchall()

            sc_lec = eval(f'{_score[0][0]}+{lec}')
            sc_sem = eval(f'{_score[0][1]}+{sem}')
            sc_lab = eval(f'{_score[0][2]}+{lab}')
            sc_prac = eval(f'{_score[0][3]}+{prac}')

            with sql.connect(SETTINGS.get('Db_name')) as con:
                cur = con.cursor()
                cur.execute(
                    """UPDATE mod_subjects SET score_lectures=?, score_seminars=?,
                    score_labs=?, score_practice=? WHERE mod_id=? AND subject=?""",
                    (sc_lec, sc_sem, sc_lab, sc_prac, _id[0], subj)
                )
                con.commit()
        else: QMessageBox.information(self, 'Внимание!', SETTINGS.get('Add_msg_4'))

    """Создает вкладку с предметами по студенту"""
    def open_stud_info(self):
        name = (self.cb_names_2.currentText()).split()
        
        if len(name) != 0:
            # Tab 2
            column_lbls = [
                'Предмет', 'Баллы за\nлекции',
                'Баллы за\nсеминары', 'Баллы за\nлабораторные',
                'Баллы за\nпрактику', 'Общие\nбаллы'
            ]
            self.TableWidget_2 = QTableWidget()
            self.TableWidget_2.setColumnCount(6)
            self.TableWidget_2.setHorizontalHeaderLabels(column_lbls)
            self.TableWidget_2.setSortingEnabled(True)

            with sql.connect(SETTINGS.get('Db_name')) as con:
                cur = con.cursor()
                cur.execute("""SELECT subject, score_lectures,
                    score_seminars, score_labs, score_practice FROM mod_subjects
                    JOIN students ON stud_id=mod_id 
                    WHERE firstname=? AND lastname=?""", (name[0], name[1]))
                con.commit()
                mod_subjects = cur.fetchall()

                count = 0
                for el in mod_subjects:
                    self.TableWidget_2.setRowCount(len(mod_subjects))

                    _subj = QTableWidgetItem(str(el[0]))
                    _sc_lec = QTableWidgetItem(str(el[1]))
                    _sc_sem = QTableWidgetItem(str(el[2]))
                    _sc_lab = QTableWidgetItem(str(el[3]))
                    _sc_prac = QTableWidgetItem(str(el[4]))
                    _sc_total = QTableWidgetItem(str(
                        eval(f'{el[1]}+{el[2]}+{el[3]}+{el[4]}'))
                    )
                    self.TableWidget_2.setItem(count, 0, _subj)
                    self.TableWidget_2.setItem(count, 1, _sc_lec)
                    self.TableWidget_2.setItem(count, 2, _sc_sem)
                    self.TableWidget_2.setItem(count, 3, _sc_lab)
                    self.TableWidget_2.setItem(count, 4, _sc_prac)
                    self.TableWidget_2.setItem(count, 5, _sc_total)

                    count += 1
                
            self.tab1_2 = QWidget()
            self.tab1_2.layout = QVBoxLayout()
            self.tab1_2.layout.addWidget(self.TableWidget_2)
            self.tab1_2.setLayout(self.tab1_2.layout)

            try: self.tabs.removeTab(1)
            
            except: print('Вкладки еще не существует')
            
            finally:
                self.tabs.insertTab(1, self.tab1_2, f'Студент: {name[0]} {name[1]}')
        else: QMessageBox.information(self, 'Внимание!', SETTINGS.get('Msg_1'))

    """Создает вкладку со студентами по предмету"""
    def open_subj_info(self):
        subject = self.cb_subjs_2.currentText()
        
        if len(subject) != 0:
            # Tab 3
            columns_lbls = [
                'Имя', 'Фамилия', 'Направление',
                'Курс', 'Общие\nбаллы'
            ]
            self.TableWidget_3 = QTableWidget()
            self.TableWidget_3.setColumnCount(5)
            self.TableWidget_3.setHorizontalHeaderLabels(columns_lbls)
            self.TableWidget_3.setSortingEnabled(True)

            with sql.connect(SETTINGS.get('Db_name')) as con:
                cur = con.cursor()
                cur.execute("""
                    SELECT firstname, lastname, direction, course, 
                    score_lectures, score_seminars, score_labs, 
                    score_practice FROM mod_subjects
                    JOIN students ON mod_id=stud_id WHERE (subject=?)""",
                    (subject,)
                )
                con.commit()
                mod_subjects = cur.fetchall()
                print(mod_subjects)

                count = 0
                for el in mod_subjects:
                    self.TableWidget_3.setRowCount(len(mod_subjects))

                    _fn = QTableWidgetItem(str(el[0]))
                    _ln = QTableWidgetItem(str(el[1]))
                    _dir = QTableWidgetItem(str(el[2]))
                    _cr = QTableWidgetItem(str(el[3]))
                    _sc_total = QTableWidgetItem(str(
                        eval(f'{el[4]}+{el[5]}+{el[6]}+{el[7]}'))
                    )
                    
                    self.TableWidget_3.setItem(count, 0, _fn)
                    self.TableWidget_3.setItem(count, 1, _ln)
                    self.TableWidget_3.setItem(count, 2, _dir)
                    self.TableWidget_3.setItem(count, 3, _cr)
                    self.TableWidget_3.setItem(count, 4, _sc_total)

                    count += 1

            self.tab1_3 = QWidget()
            self.tab1_3.layout = QVBoxLayout()
            self.tab1_3.layout.addWidget(self.TableWidget_3)
            self.tab1_3.setLayout(self.tab1_3.layout)

            try: self.tabs.removeTab(2)
            
            except: print('Вкладки еще не существует')
            
            finally: self.tabs.insertTab(2, self.tab1_3, f'Предмет: {subject}')
        else: QMessageBox.information(self, 'Внимание!', SETTINGS.get('Msg_2'))
    """/Functions"""