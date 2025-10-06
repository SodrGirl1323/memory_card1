from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
        QApplication, QWidget, 
        QHBoxLayout, QVBoxLayout, 
        QGroupBox, QButtonGroup, QRadioButton,  
        QPushButton, QLabel, QMessageBox)
from random import shuffle
class Question():    
    def __init__(self, question, right, wrong1, wrong2, wrong3):
        self.question = question
        self.right = right
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3
questions = [
    Question('2+2','4','5','6', '7'),
    Question('2^2','2*2','2+2','2*2*2', '5'),
    Question('2^0','1','0','2', '5')

] 
shuffle(questions)
def show_result():
    AnsGroupBox.show()
    RadioGroupBox.hide()
    StatisticsGroupBox.hide()
    btn_OK.setText('Следующий вопрос')
def show_question():
    AnsGroupBox.hide()
    RadioGroupBox.show()
    StatisticsGroupBox.hide()
    btn_OK.setText('Ответить')
    RadioGroup.setExclusive(False)    
    rbtn_1.setChecked(False)
    rbtn_2.setChecked(False)
    rbtn_3.setChecked(False)
    rbtn_4.setChecked(False)
    RadioGroup.setExclusive(True) 
def click_ok():
    if btn_OK.text() == 'Ответить':
        check_answer()
    elif btn_OK.text() == 'Запустить заново':
        restart()
    else:
        next_question()
def next_question():
    if window.count > len(questions)-1:
        show_statistic()
    else:
        window.total +=1
        q = questions[window.count]
        window.count +=1
        ask(q)
def answer_choice():
   choice_win = QMessageBox()
   choice_win.setText('Выбери ответ!')
   choice_win.exec_()
def show_statistic():
    AnsGroupBox.hide()
    RadioGroupBox.hide()
    StatisticsGroupBox.show()
    lb_Question.setText('')
    total_questions.setText('- Всего вопросов: '+str(window.total))
    total_right_answer.setText('- Правильных ответов: '+str(window.right))
    rating.setText('Рейтинг: '+str(window.right/window.total*100)+"%")
    btn_OK.setText('Запустить заново')
def restart():
    window.total = 0 
    window.count = 0
    window.right = 0
    shuffle(questions)
    next_question()
def ask(q:Question):
    shuffle(answers)
    answers[0].setText(q.right)
    answers[1].setText(q.wrong1)
    answers[2].setText(q.wrong2)
    answers[3].setText(q.wrong3)
    lb_Question.setText(q.question)
    lb_Correct.setText(q.right)
    show_question()
def show_correct(res):
    lb_Result.setText(res)
    show_result()
def check_answer():
    if answers[0].isChecked():
        window.right +=1
        print('Статистика')
        print('- Всего вопросов:', window.total)
        print('- Правильных ответов:', window.right)
        print('Рейтинг:', window.right/window.total*100, "%")
        show_correct('Правильно')
    elif answers[1].isChecked() or answers[2].isChecked() or answers[3].isChecked():
        show_correct('Неверно')
    else:
        answer_choice()



app = QApplication([])


app.setStyleSheet("""
    QWidget {
        background: #6D1896;
        color: white;
        font-family: Arial;
        font-size: 12pt;
    }
    
    QGroupBox {
        background: rgba(255, 255, 255, 0.2);
        border: 2px solid white;
        border-radius: 10px;
        margin-top: 1ex;
        font-weight: bold;
    }
    
    QGroupBox::title {
        subcontrol-origin: margin;
        left: 10px;
        padding: 0 3px;
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
        border: 2px solid #6D1896;
    }
    
    QRadioButton::indicator:checked {
        background: white;
        border: 2px solid #6D1896;
    }
    QPushButton {
        background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #f6f7fa, stop:1 #dadbdf);
        border: 2px solid #6D1896;
        border-radius: 10px;
        color: #6D1896;
        padding: 10px 20px;
        font-weight: bold;
        min-width: 140px;
    }
    QPushButton:hover {
        background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #dadbdf, stop:1 #f6f7fa);
    }
    QPushButton:pressed {
        background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #c4c4c4, stop:1 #e0e0e0);
    }
    QLabel {
        font-size: 14pt;
        background: transparent;
    }
    
    QLabel#lb_Question {
        font-size: 16pt;
        font-weight: bold;
        background: transparent;
    }
""")


btn_OK = QPushButton('Ответить') # кнопка ответа
lb_Question = QLabel('Самый сложный вопрос в мире!') # текст вопроса

lb_Question.setObjectName("lb_Question") 

RadioGroupBox = QGroupBox("Варианты ответов") # группа на экране для переключателей с ответами
rbtn_1 = QRadioButton('Вариант 1')
rbtn_2 = QRadioButton('Вариант 2')
rbtn_3 = QRadioButton('Вариант 3')
rbtn_4 = QRadioButton('Вариант 4')

answers = [rbtn_1, rbtn_2, rbtn_3, rbtn_4]

RadioGroup = QButtonGroup()
RadioGroup.addButton(rbtn_1)
RadioGroup.addButton(rbtn_2)
RadioGroup.addButton(rbtn_3)
RadioGroup.addButton(rbtn_4)


layout_ans1 = QHBoxLayout()   
layout_ans2 = QVBoxLayout() # вертикальные будут внутри горизонтального
layout_ans3 = QVBoxLayout()
layout_ans2.addWidget(rbtn_1) # два ответа в первый столбец
layout_ans2.addWidget(rbtn_2)
layout_ans3.addWidget(rbtn_3) # два ответа во второй столбец
layout_ans3.addWidget(rbtn_4)
layout_ans1.addLayout(layout_ans2)
layout_ans1.addLayout(layout_ans3) # разместили столбцы в одной строке
RadioGroupBox.setLayout(layout_ans1) # готова "панель" с вариантами ответов 


AnsGroupBox = QGroupBox("Результат теста")
lb_Result = QLabel('прав ты или нет?') # здесь размещается надпись "правильно" или "неправильно"
lb_Correct = QLabel('ответ будет тут!') # здесь будет написан текст правильного ответа
layout_res = QVBoxLayout()
layout_res.addStretch(1)
layout_res.addWidget(lb_Result, alignment=(Qt.AlignLeft | Qt.AlignTop))

layout_res.addWidget(lb_Correct, alignment=Qt.AlignHCenter, stretch=2)
AnsGroupBox.setLayout(layout_res)

StatisticsGroupBox = QGroupBox("Статистика")
total_questions = QLabel('- Всего вопросов:')
total_right_answer = QLabel('- Правильных ответов:')
rating = QLabel('Рейтинг:')
layout_statistic = QVBoxLayout()
layout_statistic.addWidget(total_questions, alignment=Qt.AlignLeft)
layout_statistic.addWidget(total_right_answer, alignment=Qt.AlignLeft)
layout_statistic.addWidget(rating, alignment=Qt.AlignLeft)
StatisticsGroupBox.setLayout(layout_statistic)


layout_line1 = QHBoxLayout() # вопрос
layout_line2 = QHBoxLayout() # варианты ответов или результат теста
layout_line3 = QHBoxLayout() # кнопка "Ответить"
layout_line1.addWidget(lb_Question, alignment=(Qt.AlignHCenter | Qt.AlignVCenter))
layout_line2.addWidget(RadioGroupBox)   
layout_line2.addWidget(AnsGroupBox)  
layout_line2.addWidget(StatisticsGroupBox)
StatisticsGroupBox.hide()
AnsGroupBox.hide() # скроем панель с ответом, сначала должна быть видна панель вопросов


layout_line3.addStretch(1)
layout_line3.addWidget(btn_OK, stretch=3) # кнопка должна быть большой
layout_line3.addStretch(1)


layout_card = QVBoxLayout()


layout_card.addLayout(layout_line1, stretch=2)
layout_card.addLayout(layout_line2, stretch=8)
layout_card.addStretch(1)
layout_card.addLayout(layout_line3, stretch=1)
layout_card.addStretch(1)
layout_card.setSpacing(5) # пробелы между содержимым


window = QWidget()
window.setWindowTitle('Memo Card')
window.setFixedSize(600, 500)
window.setLayout(layout_card)

window.right = 0
window.total = 0
window.count = 0 
next_question()
btn_OK.clicked.connect(click_ok)
window.show()
app.exec()


