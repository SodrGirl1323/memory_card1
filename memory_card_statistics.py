from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
        QApplication, QWidget, 
        QHBoxLayout, QVBoxLayout, 
        QGroupBox, QButtonGroup, QRadioButton,  QMessageBox,
        QPushButton, QLabel)
from random import shuffle
class Question():
    def __init__(self, question, right, wrong1, wrong2, wrong3):
        self.question = question
        self.right = right
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3
questions = [
    Question('1','1','1','1','1'),
    Question('2','2','2','2','2'),
    Question('3','3','3','3','3')

]
shuffle(questions)
def show_result():
    RadioGroupBox.hide()
    StatisticsGroupBox.hide()
    AnsGroupBox.show()
    btn_OK.setText('Следующий вопрос')
def show_question():
    RadioGroupBox.show()
    StatisticsGroupBox.hide()
    AnsGroupBox.hide()
    btn_OK.setText('Ответить')
    RadioGroup.setExclusive(False)    
    rbtn_1.setChecked(False)
    rbtn_2.setChecked(False)
    rbtn_3.setChecked(False)
    rbtn_4.setChecked(False)
    RadioGroup.setExclusive(True) 
def  click_ok():
    if btn_OK.text() == 'Ответить':
        check_answer()
    elif btn_OK.text() == 'Начать заново':
        restart()
    else:
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
    print('Статистика')
    print('- Всего вопросов:', window.total)
    print('- Правильных ответов:', window.right)
    print('Рейтинг:', window.right/window.total*100, "%")
    lb_Result.setText(res)
    show_result()
def check_answer():
    if answers[0].isChecked():
        window.right +=1
        show_correct('Правильно')
    elif answers[1].isChecked() or answers[2].isChecked() or answers[3].isChecked():
        show_correct('Неверно')
    else:
        answer_choice()
def answer_choice():
   choice_win = QMessageBox()
   choice_win.setText('Выбери ответ!')
   choice_win.exec_()
def next_question():
    if window.total >= len(questions):
        show_statistics()
    else:
        q = questions[window.total]
        window.total +=1
        ask(q)
def show_statistics():
    RadioGroupBox.hide()
    AnsGroupBox.hide()
    StatisticsGroupBox.show()
    btn_OK.setText('Начать заново')
    lb_Question.setText('')
    lb_total_question.setText('- Всего вопросов: ' + str(window.total))
    lb_right_answer.setText('- Правильных ответов: ' + str(window.right))
    ld_rating.setText('Рейтинг: '+  str(window.right/window.total*100) + "%")
def restart():
    window.total = 0 
    window.count = 0
    window.right = 0
    shuffle(questions)
    next_question()

app = QApplication([])
btn_OK = QPushButton('Ответить') # кнопка ответа
lb_Question = QLabel('Самый сложный вопрос в мире!') # текст вопроса

RadioGroupBox = QGroupBox("Варианты ответов") # группа на экране для переключателей с ответами
rbtn_1 = QRadioButton('Вариант 1')
rbtn_2 = QRadioButton('Вариант 2')
rbtn_3 = QRadioButton('Вариант 3')
rbtn_4 = QRadioButton('Вариант 4')
answers = [rbtn_1,rbtn_2,rbtn_3,rbtn_4]
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
layout_res.addWidget(lb_Result, alignment=(Qt.AlignLeft | Qt.AlignTop))
layout_res.addWidget(lb_Correct, alignment=Qt.AlignHCenter, stretch=2)
AnsGroupBox.setLayout(layout_res)

StatisticsGroupBox = QGroupBox("Статистика")
lb_total_question = QLabel('- Всего вопросов:')
lb_right_answer = QLabel('- Правильных ответов:')
ld_rating = QLabel('Рейтинг:')
layout_statistics = QVBoxLayout()
layout_statistics.addWidget(lb_total_question, alignment=Qt.AlignLeft)
layout_statistics.addWidget(lb_right_answer, alignment=Qt.AlignLeft)
layout_statistics.addWidget(ld_rating, alignment=Qt.AlignLeft)
StatisticsGroupBox.setLayout(layout_statistics)

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
window.resize(500, 400)
window.setLayout(layout_card)
window.total = 0
window.right = 0
next_question()
btn_OK.clicked.connect(click_ok)

window.show()
app.exec()


