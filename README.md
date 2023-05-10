# Database for University
by WoollySensed Software (ВуллиСэнсэд Софтвэйр)

# Небольшое отступление
Проект написан на языке **Python3** (3.11) с использованием фреймворка **PyQt5**, для отрисовки GUI, и **SQLite3**, в качестве СУБД.

Это мой первый проект такого масштаба, поэтому все замечания по поводу структуру кода с радостью приму во внимание. Изначально проект был написан с использованием Tkinter'а, из-за чего функционал был ограничен. Но достаточно изучив фреймворк PyQt5, для написания подобного проекта, появился необходимый мне функционал.

# Структура проекта
`main.py` - основной файл, запускающий все необходимые зависимости.

`settings.py` - содержит словарь с необходимым набором ключей и переменную, содержащую CSS код для стилизации.

`MainWin.py` - отрисовывает основное окно, содержит методы для добавления студента в БД и удаления из нее.

`DatabaseWin.py` - отрисовывает дочернее окно, содержит методы для отображения главной таблицы, таблицы с информацией по студенту и информацией по предмету. Также метод для добавления нужного предмета в БД.

`Handler.py` - создает файл с базой данных, таблицу со студентами и таблицу с предметами и баллами по ним. 

# Необходимое для запуска проекта
**PyQt5 5.15.9**
`pip install PyQt5`

**pyqt5-tools 5.15.9.3.3**
`pip install pyqt5-tools`

Если не установлено, то **SQLite3-0611 0.0.1**
`pip install SQLite3-0611`
