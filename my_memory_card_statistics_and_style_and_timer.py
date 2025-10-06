from PyQt5.QtCore import Qt, QTime, QTimer
from PyQt5.QtWidgets import QButtonGroup, QApplication, QGroupBox, QPushButton, QWidget, QLabel, QHBoxLayout, QVBoxLayout, QMessageBox, QRadioButton
from random import shuffle
start_time = QTime(0, 0, 0)
class Question():
    def __init__(self, question, right, wrong1, wrong2, wrong3):
        self.question = question
        self.right = right
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3

def show_result():
    RadioGroupBox.hide()
    StatisticsGroup.hide()
    RadioGroupBox2.show()
    ansButton.setText('Следующий вопрос')
def show_question():
    RadioGroupBox2.hide()
    RadioGroupBox.show()
    StatisticsGroup.hide()
    ansButton.setText('Ответить')
    RadioGroup.setExclusive(False)
    rbtn_1.setChecked(False)
    rbtn_2.setChecked(False)
    rbtn_3.setChecked(False)
    rbtn_4.setChecked(False)
    RadioGroup.setExclusive(True)
def start_test():
    if ansButton.text() == 'Ответить':
        check_answer()
    elif ansButton.text() == 'Начать заново':
        restart()
    else:
        next_question()
def ask(q: Question):
    shuffle(answers)
    answers[0].setText(q.right)
    answers[1].setText(q.wrong1)
    answers[2].setText(q.wrong2)
    answers[3].setText(q.wrong3)
    ib_question.setText(q.question)
    text2.setText(q.right)
    show_question()
def show_correct(res):        
    print('Статистика')
    print('- Всего вопросов:', main_win.total)
    print('- Правельных ответов:', main_win.right)
    print('Рейтинг', main_win.right/main_win.total*100, "%")
    text.setText(res)
    show_result()
def check_answer():
    if answers[0].isChecked():
        main_win.right +=1
        show_correct('Правильно!')
    elif answers[1].isChecked() or answers[2].isChecked() or answers[3].isChecked():
        show_correct('Неверно!')
    else:
        answer_choice()
def answer_choice():
    choice_win = QMessageBox()
    choice_win.setText('Выбери Ответ!!!')
    choice_win.exec()
def next_question():
    if main_win.count == 0:
        start_timer()
    if main_win.count > len(questions)-1:
        show_statistics()
    else:
        main_win.total +=1
        q = questions[main_win.count]
        main_win.count += 1
        ask(q)
def restart():
    global start_time
    main_win.total = 0
    main_win.count = 0
    main_win.right = 0
    shuffle(questions)
    start_time = QTime(0, 0)
    start_timer()
    next_question()
def show_statistics():
    stop_timer()
    RadioGroupBox.hide()
    RadioGroupBox2.hide()
    StatisticsGroup.show()
    ansButton.setText('Начать заново')
    ib_question.setText('')
    ib_total_question.setText('- Всего вопросов:' + str(main_win.total))
    ib_right_answer.setText('- Правильных ответов:' + str(main_win.right))
    ib_rating.setText('- Рэйтинг:' + str(main_win.right/main_win.total*100) + "%")
    spent_time.setText('- Затраченное время:' + start_time.toString("mm:ss"))
questions = [
    Question('1+1', '2', '3', '4', '5'),
    Question('2+2', '4', '5', '6', '7')

    ]
#Question('3+3', '6', '7', '8', '9'),
#Question('4+4', '8', '9', '10', '11'),
#Question('5+5', '10', '11', '12', '13'),
#Question('6+6', '12', '13', '14', '15'),
#Question('7+7', '14', '15', '16', '17'),
#Question('8+8', '16', '17', '18', '19'),
#Question('9+9', '18', '20', '19', '21'),
#Question('10+10', '20', '21', '22', '23')

shuffle(questions)
app = QApplication([])
main_win =  QWidget()
main_win.setFixedSize(600, 500)
main_win.setWindowTitle('Memory Card')

timer = QTimer()
start_time = QTime(0,0)
time_label = QLabel('Время: 00:00')
time_label.setAlignment(Qt.AlignRight | Qt.AlignCenter)

def update_timer():
    global start_time
    start_time = start_time.addSecs(1)
    time_label.setText(f'Время:{start_time.toString("mm:ss")}')

def start_timer():
    global start_time
    timer.stop()  
    start_time = QTime(0, 0)
    time_label.setText('Время: 00:00')
    try:
        timer.timeout.disconnect() 
    except TypeError:
        pass  
    timer.timeout.connect(update_timer)
    timer.start(1000)

def stop_timer():
    timer.stop()

app.setStyleSheet("""
    QWidget { 
        background: #ffb3da;
        color: #660033;
        font-famyly: Arial;
        font-size: 12pt
    }
    QGroupBox {
        background: rgba(255, 255, 153, 0.2);
        bolder: 2px solid white;
        border-radius: 10px;
        margin-top: 1ex;
        font-weight: bold;
    }
    QGoupBox::title {
        subcontrol-origin: margin;
        left: 10px;
        padding:  0 3px;
        color: white;
    }
    QRadioButton {
        padding: 5px;
        background: transparent;
    }
    QRadioButton::indicator {
        width: 20px;
        height: 20px;
        border-radius: 10px;
        border: 2px solid #ff00ff;
    }
    QRadioButton::indicator:checked{
        background: white;
        border: 2px solid #99bbff;
    }
    QPushButton {
        background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #ff0066, stop:1 #ffb3d1);
        border: 2px solid #ff00ff;
        border-radius: 10px;
        padding: 10px 20px;
        font-weight: bold;
        min-width: 160px;
    }
    QPushButton:hover {
        background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #1aa3ff, stop:1 #005c99) 

    }
    QPushButton:pressed {
        background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #ffff99, stop:1 #ffff4d)

    }
    QLabel {
        font-size: 14pt;
        background: transparent;

    }
    QLabel#ib_question{
        font-size: 16pt;
        font-weight: bold;
        background: transparent;
    }
    """)
ib_question = QLabel('?')
ib_question.setWordWrap(True)
ib_question.setObjectName("ib_question")
ansButton = QPushButton('Ответить')

RadioGroupBox = QGroupBox('Варианты ответов')
rbtn_1 = QRadioButton('1')
rbtn_2 = QRadioButton('2')
rbtn_3 = QRadioButton('3')
rbtn_4 = QRadioButton('4')
answers = [rbtn_1, rbtn_2, rbtn_3, rbtn_4]

RadioGroup = QButtonGroup()
RadioGroup.addButton(rbtn_1)
RadioGroup.addButton(rbtn_2)
RadioGroup.addButton(rbtn_3)
RadioGroup.addButton(rbtn_4)

layout_a1 = QHBoxLayout()
layout_a2 = QVBoxLayout()
layout_a3 = QVBoxLayout()

layout_a2.addWidget(rbtn_1)
layout_a2.addWidget(rbtn_2)
layout_a3.addWidget(rbtn_3)
layout_a3.addWidget(rbtn_4)
layout_a1.addLayout(layout_a2)
layout_a1.addLayout(layout_a3)

RadioGroupBox.setLayout(layout_a1)

RadioGroupBox2 = QGroupBox('Результат теста')
text = QLabel('Правельно/Неправильно')
text2 = QLabel('Правильный ответ')

layoutB = QVBoxLayout()
layoutB.addStretch(1)
layoutB.addWidget(text, alignment = (Qt.AlignLeft | Qt.AlignTop))
layoutB.addWidget(text2, alignment = Qt.AlignCenter, stretch = 2)
RadioGroupBox2.setLayout(layoutB)

StatisticsGroup = QGroupBox("  Статистика")
ib_total_question = QLabel('Всего вопросов')
ib_right_answer = QLabel('- Правильных ответов')
ib_rating = QLabel('Рэйтинг')
spent_time = QLabel('- Затраченное время:' + start_time.toString("mm:ss"))
layout_stas = QVBoxLayout()
#layout_stas.addStretch(1)
layout_stas.addWidget(ib_total_question, alignment = Qt.AlignLeft)
layout_stas.addWidget(ib_right_answer, alignment = Qt.AlignLeft)
layout_stas.addWidget(ib_rating, alignment = Qt.AlignLeft)
layout_stas.addWidget(spent_time, alignment = Qt.AlignLeft)
StatisticsGroup.setLayout(layout_stas)

main_lay_H1 = QHBoxLayout()
main_lay_H2 = QHBoxLayout()
main_lay_H3 = QHBoxLayout()

main_lay_V = QVBoxLayout()

main_lay_H1.addWidget(ib_question, alignment=(Qt.AlignHCenter | Qt.AlignVCenter))
main_lay_H1.addStretch(1)
main_lay_H1.addWidget(time_label)

main_lay_H1.addWidget(ib_question, alignment = Qt.AlignCenter)
main_lay_H2.addWidget(RadioGroupBox)
main_lay_H2.addWidget(RadioGroupBox2)
main_lay_H2.addWidget(StatisticsGroup)
StatisticsGroup.hide()
RadioGroupBox2.hide()

main_lay_H3.addStretch(1)
main_lay_H3.addWidget(ansButton, stretch = 4)
main_lay_H3.addStretch(1)

main_lay_V.addLayout(main_lay_H1, stretch = 2)
main_lay_V.addLayout(main_lay_H2, stretch = 8)
main_lay_V.addStretch(1)
main_lay_V.addLayout(main_lay_H3, stretch = 1)
main_lay_V.addStretch(1)
main_lay_V.setSpacing(5)
main_win.setLayout(main_lay_V)

main_win.total = 0
main_win.right = 0
main_win.count = 0
next_question()
ansButton.clicked.connect(start_test)

start_timer()
main_win.show()
app.exec_()