SETTINGS = {
    'Version': '8.4.1',
    'Db_name': 'db.sqlite3',
    'About_msg': """
    "WoollySensed Software" (ВуллиСэнсэд Софтвэйр) -
    небольшая команда, которая горит своим делом.
    
    Помощь в создании оказали:
        - Дарья Лапшина (Дизайн)
        - Диана Пулина (Дизайн)
        - Руслан Лебедев (Дизайн)

    Об обновлении (8.4.0):
        - Программа была перенесена на
           новый фреймворк (PyQt5).
        - Переосмыслены и переработаны окна
           главного меня и базы дынных.
        - Переосмыслены и переработаны функции
           для работы с базой данных.
        - Изменена цветовая гамма интерфейса.

    Обратная связь с нами:
        почта: woharkte.onion@gmail.com
    """,
    'Info_msg': """
        Программа базируется на балльной системе оценивания,
        поэтому при необходимости использовать обычные оценки,
        рекомендуется держать "баллы" в диапазоне 1-5.

        В данном разделе можно добавить или убавить баллы по
        предмету, который бы выбран. Чтобы убавить баллы
        укажите знак "-" перед значением. (Пример: -2)

        Внимание! Чтобы программа корректно выполнила запрос,
        необходимо заполнить все поля с баллами. 
        Если указывать все поля Вам не нужно, внесите туда ноль!
    """,
    'Add_msg_1': """
        Проверьте, что Вы ввели все данные, и попробуйте снова!
        Студент занесется в базу данных только при
        наличии всех необходимых данных.
    """,
    'Add_msg_2': """
        Строка для ввода курса принимает только цифры!

        Нельзя указывать:
        - буквы
        - спец. символы
    """,
    'Add_msg_3': """
        Для добавления предмета необходимо ввести
        его наименование!
    """,
    'Add_msg_4': """
        Чтобы добавить или убавить баллы по предмету,
        необходимо заполнить все поля с баллами!
    """,
    'Del_msg_1': """
        Студент был удален из базы данных вместе
        с его успеваемостью.

        Для корректного отображения информации в базе данных
        необходимо закрыть окно базы данных, если оно было
        открыто, и открыть, если это необходимо!
    """,
    'Del_msg_2': """
        Проверьте, что Вы ввели все данные, и попробуйте снова!
        Студент удалится из базы данных только при
        наличии всех необходимых данных.
    """,
    'Msg_1': """
        Операция не может быть выполнена, т.к. список студентов пуст.
    """,
    'Msg_2': """
        Операция не может быть выполнена, т.к. список предметов пуст.
    """,
}

STYLE = """
    QWidget#Db_Window{
        background: #343333;
        font-family: Courier;
    }
    QLabel#Db_Label{
        background: #343333;
        color: #FFFFFF;
        border: 1px solid #FF0000;
    }
    QComboBox#Db_ComboBox{
        background: #343333;
        color: #FFFFFF;
        border: 1px solid #FF0000;
        selection-color: #FFFFFF;
    }
    QComboBox#Db_ComboBox QAbstractItemView#Db_ComboBox {
        background-color: #343333;
    }
    QComboBox#Db_ComboBox:hover{
        background: #FF0000;
        color: #FFFFFF;
    }
    QLineEdit#Db_LineEdit{
        background: #343333;
        color: #FFFFFF;
        border: 1px solid #FF0000;
    }
    QPushButton#Db_Button{
        background: #FF0000;
        padding: 1px;
        color: #FFFFFF;
        border-radius: 10px;
        font: bold;
    }
    QPushButton#Db_Button:hover{
        background: #800000;
        color: #FFFFFF;
    }

    QWidget#Main_Window{
        background: #343333;
    }
    QLineEdit#Main_LineEdit{
        background: #343333;
        color: #FFFFFF;
        padding: 1px;
        border: 1px solid #FF0000;
        border-radius: 8px;
    }
    QPushButton#Main_Button:hover{
        background: #800000;
        color: #FFFFFF;
    }
    QPushButton#Main_Button{
        background: #FF0000;
        padding: 1px;
        color: #FFFFFF;
        border-radius: 10px;
        font: bold;
        font-family: Courier;
    }
    QPushButton#About_Button{
        background: #343333;
        color: #FFFFFF;
    }
    QPushButton#About_Button:hover{
        background: #FFFFFF;
        color: #FF0000;
    }
    QMessageBox{
        background-color: #343333;
    }
    QMessageBox QLabel{
        color: #FFFFFF;
    }
    QMessageBox QPushButton{
        background: #FF0000;
        color: #FFFFFF;
    }
"""
