<!-- TOC -->

- [Label](#label)
    - [打开文件超链接](#打开文件超链接)
    - [快捷键关联](#快捷键关联)
- [QLineEdit](#qlineedit)
    - [设置密码是否显示](#设置密码是否显示)
    - [验证器](#验证器)
    - [输入掩码](#输入掩码)
    - [综合示例](#综合示例)
- [QTextEdit](#qtextedit)
- [QPushButton](#qpushbutton)

<!-- /TOC -->
# Label
## 打开文件超链接
```python
# -*- coding: utf-8 -*-


'''
    【简介】
	PyQT5中Qlabel例子

'''

from PyQt5.QtWidgets import QApplication, QLabel, QWidget, QVBoxLayout
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap, QPalette
import sys


class WindowDemo(QWidget):
    def __init__(self):
        super().__init__()

        label1 = QLabel(self)
        label2 = QLabel(self)
        label3 = QLabel(self)
        label4 = QLabel(self)

        # 1
        label1.setText("这是一个文本标签。")
        label1.setAutoFillBackground(True)
        palette = QPalette()
        palette.setColor(QPalette.Window, Qt.blue)
        label1.setPalette(palette)
        label1.setAlignment(Qt.AlignCenter)

        label2.setText("<a href='#'>欢迎使用Python GUI 应用</a>")

        label3.setAlignment(Qt.AlignCenter)
        label3.setToolTip('这是一个图片标签')
        label3.setPixmap(QPixmap("./images/python.jpg"))

        label4.setText("<A href='http://www.cnblogs.com/wangshuo1/'>欢迎访问信平的小屋</a>")
        label4.setAlignment(Qt.AlignRight)
        label4.setToolTip('这是一个超链接标签')

        # 2
        vbox = QVBoxLayout()
        vbox.addWidget(label1)
        vbox.addStretch()
        vbox.addWidget(label2)
        vbox.addStretch()
        vbox.addWidget(label3)
        vbox.addStretch()
        vbox.addWidget(label4)

        # 3
        label1.setOpenExternalLinks(True)
        # 打开允许访问超链接,默认是不允许，需要使用 setOpenExternalLinks(True)允许浏览器访问超链接
        label4.setOpenExternalLinks(True)
        # 点击文本框绑定槽事件
        label4.linkActivated.connect(link_clicked)

        # 划过文本框绑定槽事件
        label2.linkHovered.connect(link_hovered)
        label1.setTextInteractionFlags(Qt.TextSelectableByMouse)

        self.setLayout(vbox)
        self.setWindowTitle("QLabel 例子")


def link_hovered():
    print("当鼠标滑过label-2标签时，触发事件。")


def link_clicked():
    print("当鼠标点击label-4标签时，触发事件。")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = WindowDemo()
    win.show()
    sys.exit(app.exec_())
```

## 快捷键关联
按住`alt`+`N`可以切到`Name`，`alt`+`p`可以切换到`password`，使用了网格布局。
```python
# -*- coding: utf-8 -*-

'''
    【简介】
	PyQt5中Qlabel例子
   按住 Alt + N , Alt + P , Alt + O , Alt + C 切换组件控件
  
'''

from PyQt5.QtWidgets import *
import sys  
    
class QlabelDemo(QDialog):  
    def __init__(self ):  
        super().__init__()
         
        self.setWindowTitle('Qlabel 例子')
        nameLb1 = QLabel('&Name', self)
        nameEd1 = QLineEdit( self )
        nameLb1.setBuddy(nameEd1)
        
        nameLb2 = QLabel('&Password', self)
        nameEd2 = QLineEdit( self )
        nameLb2.setBuddy(nameEd2)
        
        btnOk = QPushButton('&OK')
        btnCancel = QPushButton('&Cancel')
        mainLayout = QGridLayout(self)
        mainLayout.addWidget(nameLb1,0,0)
        mainLayout.addWidget(nameEd1,0,1,1,2)
        
        mainLayout.addWidget(nameLb2,1,0)
        mainLayout.addWidget(nameEd2,1,1,1,2)
         
        mainLayout.addWidget(btnOk,2,1)
        mainLayout.addWidget(btnCancel,2,2) 
  
if __name__ == "__main__":  
    app = QApplication(sys.argv)  
    labelDemo = QlabelDemo()  
    labelDemo.show()  
    sys.exit(app.exec_())
```

# QLineEdit
## 设置密码是否显示
```python
# -*- coding: utf-8 -*-

'''
    【简介】
	PyQt5中 QLineEdit.EchoMode效果例子

'''

from PyQt5.QtWidgets import QApplication, QLineEdit, QWidget, QFormLayout
import sys


class lineEditDemo(QWidget):
    def __init__(self, parent=None):
        super(lineEditDemo, self).__init__(parent)
        self.setWindowTitle("QLineEdit例子")

        flo = QFormLayout()
        pNormalLineEdit = QLineEdit()
        pNoEchoLineEdit = QLineEdit()
        pPasswordLineEdit = QLineEdit()
        pPasswordEchoOnEditLineEdit = QLineEdit()

        flo.addRow("Normal", pNormalLineEdit)
        flo.addRow("NoEcho", pNoEchoLineEdit)
        flo.addRow("Password", pPasswordLineEdit)
        flo.addRow("PasswordEchoOnEdit", pPasswordEchoOnEditLineEdit)

        pNormalLineEdit.setPlaceholderText("Normal")
        pNoEchoLineEdit.setPlaceholderText("NoEcho")
        pPasswordLineEdit.setPlaceholderText("Password")
        pPasswordEchoOnEditLineEdit.setPlaceholderText("PasswordEchoOnEdit")

        # 设置显示效果
        pNormalLineEdit.setEchoMode(QLineEdit.Normal)
        pNoEchoLineEdit.setEchoMode(QLineEdit.NoEcho)
        pPasswordLineEdit.setEchoMode(QLineEdit.Password)
        pPasswordEchoOnEditLineEdit.setEchoMode(QLineEdit.PasswordEchoOnEdit)

        self.setLayout(flo)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = lineEditDemo()
    win.show()
    sys.exit(app.exec_())
```

## 验证器
```python
# -*- coding: utf-8 -*-

'''
    【简介】
	PyQt5中 QLineEdit的验证器例子

'''

from PyQt5.QtWidgets import QApplication, QLineEdit, QWidget, QFormLayout
from PyQt5.QtGui import QIntValidator, QDoubleValidator, QRegExpValidator
from PyQt5.QtCore import QRegExp
import sys


class lineEditDemo(QWidget):
    def __init__(self, parent=None):
        super(lineEditDemo, self).__init__(parent)
        self.setWindowTitle("QLineEdit例子")

        flo = QFormLayout()
        pIntLineEdit = QLineEdit()
        pDoubleLineEdit = QLineEdit()
        pValidatorLineEdit = QLineEdit()

        flo.addRow("整形", pIntLineEdit)
        flo.addRow("浮点型", pDoubleLineEdit)
        flo.addRow("字母和数字", pValidatorLineEdit)

        pIntLineEdit.setPlaceholderText("整形");
        pDoubleLineEdit.setPlaceholderText("浮点型");
        pValidatorLineEdit.setPlaceholderText("字母和数字");

        # 整形 范围：[1, 99]
        pIntValidator = QIntValidator(self)
        pIntValidator.setRange(1, 99)

        # 浮点型 范围：[-360, 360] 精度：小数点后2位
        pDoubleValidator = QDoubleValidator(self)
        pDoubleValidator.setRange(-360, 360)
        pDoubleValidator.setNotation(QDoubleValidator.StandardNotation)
        pDoubleValidator.setDecimals(2)

        # 字符和数字
        reg = QRegExp("[a-zA-Z0-9]+$")
        pValidator = QRegExpValidator(self)
        pValidator.setRegExp(reg)

        # 设置验证器
        pIntLineEdit.setValidator(pIntValidator)
        pDoubleLineEdit.setValidator(pDoubleValidator)
        pValidatorLineEdit.setValidator(pValidator)

        self.setLayout(flo)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = lineEditDemo()
    win.show()
    sys.exit(app.exec_())
```

## 输入掩码
```python
# -*- coding: utf-8 -*-

'''
    【简介】
	PyQt5中 QLineEdit的输入掩码例子

'''

from PyQt5.QtWidgets import QApplication, QLineEdit, QWidget, QFormLayout
import sys


class lineEditDemo(QWidget):
    def __init__(self, parent=None):
        super(lineEditDemo, self).__init__(parent)
        self.setWindowTitle("QLineEdit的输入掩码例子")

        flo = QFormLayout()
        pIPLineEdit = QLineEdit()
        pMACLineEdit = QLineEdit()
        pDateLineEdit = QLineEdit()
        pLicenseLineEdit = QLineEdit()

        pIPLineEdit.setInputMask("000.000.000.000;_")
        pMACLineEdit.setInputMask("HH:HH:HH:HH:HH:HH;_")
        pDateLineEdit.setInputMask("0000-00-00")
        pLicenseLineEdit.setInputMask(">AAAAA-AAAAA-AAAAA-AAAAA-AAAAA;#")

        flo.addRow("数字掩码", pIPLineEdit)
        flo.addRow("Mac掩码", pMACLineEdit)
        flo.addRow("日期掩码", pDateLineEdit)
        flo.addRow("许可证掩码", pLicenseLineEdit)

        # pIPLineEdit.setPlaceholderText("111")
        # pMACLineEdit.setPlaceholderText("222")
        # pLicenseLineEdit.setPlaceholderText("333")
        # pLicenseLineEdit.setPlaceholderText("444")

        self.setLayout(flo)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = lineEditDemo()
    win.show()
    sys.exit(app.exec_())
```

## 综合示例
```python
# -*- coding: utf-8 -*-

'''
    【简介】
	PyQt5中 QLineEdit例子

'''

from PyQt5.QtWidgets import QApplication, QLineEdit, QWidget, QFormLayout
from PyQt5.QtGui import QIntValidator, QDoubleValidator, QFont
from PyQt5.QtCore import Qt
import sys


class lineEditDemo(QWidget):
    def __init__(self, parent=None):
        super(lineEditDemo, self).__init__(parent)
        e1 = QLineEdit()
        e1.setValidator(QIntValidator())
        e1.setMaxLength(4)
        e1.setAlignment(Qt.AlignRight)
        e1.setFont(QFont("Arial", 20))
        e2 = QLineEdit()
        e2.setValidator(QDoubleValidator(0.99, 99.99, 2))
        flo = QFormLayout()
        flo.addRow("integer validator", e1)
        flo.addRow("Double validator", e2)
        e3 = QLineEdit()
        e3.setInputMask('+99_9999_999999')
        flo.addRow("Input Mask", e3)
        e4 = QLineEdit()
        e4.textChanged.connect(self.textchanged)
        flo.addRow("Text changed", e4)
        e5 = QLineEdit()
        e5.setEchoMode(QLineEdit.Password)
        flo.addRow("Password", e5)
        e6 = QLineEdit("Hello PyQt5")
        e6.setReadOnly(True)
        flo.addRow("Read Only", e6)
        e5.editingFinished.connect(self.enterPress)
        self.setLayout(flo)
        self.setWindowTitle("QLineEdit例子")

    def textchanged(self, text):
        print("输入的内容为: " + text)

    def enterPress(self):
        print("已输入值")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = lineEditDemo()
    win.show()
    sys.exit(app.exec_())
```

# QTextEdit
```python
# -*- coding: utf-8 -*-

'''
    【简介】
	PyQt5中 QTextEdit例子

'''

from PyQt5.QtWidgets import QApplication, QWidget, QTextEdit, QVBoxLayout, QPushButton
import sys


class TextEditDemo(QWidget):
    def __init__(self, parent=None):
        super(TextEditDemo, self).__init__(parent)
        self.setWindowTitle("QTextEdit 例子")
        self.resize(300, 270)
        self.textEdit = QTextEdit()
        self.btnPress1 = QPushButton("显示文本")
        self.btnPress2 = QPushButton("显示HTML")
        layout = QVBoxLayout()
        layout.addWidget(self.textEdit)
        layout.addWidget(self.btnPress1)
        layout.addWidget(self.btnPress2)
        self.setLayout(layout)
        self.btnPress1.clicked.connect(self.btnPress1_Clicked)
        self.btnPress2.clicked.connect(self.btnPress2_Clicked)

    def btnPress1_Clicked(self):
        self.textEdit.setPlainText("Hello PyQt5!\n点击按钮")

    def btnPress2_Clicked(self):
        self.textEdit.setHtml("<font color='red' size='6'><red>Hello PyQt5!\n点击按钮。</font>")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = TextEditDemo()
    win.show()
    sys.exit(app.exec_())
```

# QPushButton
```python
# -*- coding: utf-8 -*-

'''
    【简介】
	PyQt5中QButton例子


'''

import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class Form(QDialog):
    def __init__(self, parent=None):
        super(Form, self).__init__(parent)
        layout = QVBoxLayout()

        self.btn1 = QPushButton("Button1")
        self.btn1.setCheckable(True)
        self.btn1.toggle()
        self.btn1.clicked.connect(lambda: self.whichbtn(self.btn1))
        self.btn1.clicked.connect(self.btnstate)
        layout.addWidget(self.btn1)

        self.btn2 = QPushButton('image')
        self.btn2.setIcon(QIcon(QPixmap("./images/python.png")))
        self.btn2.clicked.connect(lambda: self.whichbtn(self.btn2))
        layout.addWidget(self.btn2)
        self.setLayout(layout)

        self.btn3 = QPushButton("Disabled")
        self.btn3.setEnabled(False)
        layout.addWidget(self.btn3)

        self.btn4 = QPushButton("&Download")
        self.btn4.setDefault(True)
        self.btn4.clicked.connect(lambda: self.whichbtn(self.btn4))
        layout.addWidget(self.btn4)
        self.setWindowTitle("Button demo")

    def btnstate(self):
        if self.btn1.isChecked():
            print("button pressed")
        else:
            print("button released")

    def whichbtn(self, btn):
        print("clicked button is " + btn.text())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    btnDemo = Form()
    btnDemo.show()
    sys.exit(app.exec_())

```