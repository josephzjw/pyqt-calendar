import sys
from PyQt5.QtCore import QDate
from PyQt5.QtWidgets import (QWidget, QLabel, QCalendarWidget, QVBoxLayout, QApplication, QInputDialog, QPushButton)
import os
import pickle



class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.data_path = 'calendar_events.pkl'
        if not os.path.exists(self.data_path):
            self.data = dict()
            pickle.dump(self.data, open(self.data_path, 'wb'))
            print('create data first time!')
        else:
            self.data = pickle.load(open(self.data_path, 'rb'))
            print('load existing data!')
        vbox = QVBoxLayout(self)

        cal = QCalendarWidget(self)
        cal.setGridVisible(True)
        cal.clicked[QDate].connect(self.showDate)

        vbox.addWidget(cal)

        self.lbl = QLabel(self)

        date = cal.selectedDate()
        self.btn = QPushButton('点击以修改事项', self)
        self.btn.clicked.connect(self.setEvent)
        self.lbl.setText(date.toString())
        vbox.addWidget(self.btn)
        vbox.addWidget(self.lbl)

        self.setLayout(vbox)

        self.setGeometry(300, 300, 350, 300)
        self.setWindowTitle('Calendar')
        self.cnt = 0
        self.show()

    def showDate(self, date):
        # text, ok = QInputDialog.getText(self, "Input Dialog", "Enter your name:")
        # if ok:
        #     self.lbl.setText(text)
        key = date.toString("yyyy-MM-dd")
        # print(date.toString("yyyy-MM-dd"))
        if key not in self.data:
            self.lbl.setText("今日无事发生！")
        else:
            self.lbl.setText(f'{self.cnt}')

    def setEvent(self):
        text, ok = QInputDialog.getText(self, "Input Dialog", "Enter your name:")
        if ok:
            self.lbl.setText(text)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())