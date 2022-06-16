#
#tarik
#

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 300)

        self.formLayout = QtWidgets.QFormLayout(Form)
        self.formLayout.setObjectName("formLayout")

        self.textEdit = QtWidgets.QTextEdit(Form)
        self.textEdit.setObjectName("textEdit")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.SpanningRole, self.textEdit)

        self.enter_number_label = QtWidgets.QLabel(Form)
        self.enter_number_label.setObjectName("enter_number_label")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.enter_number_label)

        self.number_line_edit = QtWidgets.QLineEdit(Form)
        self.number_line_edit.setObjectName("number_line_edit")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.number_line_edit)

        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")

        self.comboBox = QtWidgets.QComboBox(Form)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.horizontalLayout.addWidget(self.comboBox)

        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setMaximumSize(QtCore.QSize(75, 16777215))
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)

        self.formLayout.setLayout(2, QtWidgets.QFormLayout.SpanningRole, self.horizontalLayout)

        self.status_label = QtWidgets.QLabel(Form)
        self.status_label.setObjectName("status_label")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.status_label)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

        #Actions
        self.comboBox.currentTextChanged['QString'].connect(self.status_label.setText)
        self.pushButton.clicked.connect(self.find_prime)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.enter_number_label.setText(_translate("Form", "Enter Number"))
        self.comboBox.setItemText(0, _translate("Form", "Print the text box"))
        self.comboBox.setItemText(1, _translate("Form", "Write the file"))
        self.pushButton.setText(_translate("Form", "RUN"))
        self.status_label.setText(_translate("Form", "Status"))
    
    def print_to_text(self):
        self.textEdit.setText(self.a)

    def find_prime(self):
        
        y = 0
        self.a = ""
        for num in range(2, int(self.number_line_edit.text()) + 1):
        # all prime numbers are greater than 1
            if num > 1:
                for i in range(2, num):
                    if (num % i) == 0:
                        break
            else:
                self.a[y] = num
                y = y+1
        self.print_to_text()



import sys

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    ex = Ui_Form()
    w = QtWidgets.QWidget()
    ex.setupUi(w)
    w.show()
    sys.exit(app.exec_())