# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'window.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import urllib.request, json, ssl, datetime, base64, os

from PyQt5.QtGui import QIcon

ssl._create_default_https_context = ssl._create_unverified_context


class Ui_MCInfo(object):
    def setupUi(self, MCInfo):
        MCInfo.setObjectName("MCInfo")
        MCInfo.resize(270, 290)
        import os.path as path
        bundle_dir = getattr(sys, '_MEIPASS', path.abspath(path.dirname(__file__)))
        data_path = os.path.abspath(path.join(bundle_dir, 'icon.png'))
        MCInfo.setWindowIcon(QIcon(f"{data_path}"))
        self.centralwidget = QtWidgets.QWidget(MCInfo)
        self.centralwidget.setObjectName("centralwidget")
        self.textEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(10, 250, 171, 31))
        self.textEdit.textChanged[str].connect(self.textChanged)
        font = QtGui.QFont()
        font.setFamily("맑은 고딕")
        font.setPointSize(11)
        self.textEdit.setFont(font)
        self.textEdit.setObjectName("textEdit")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setEnabled(False)
        self.pushButton.setGeometry(QtCore.QRect(190, 250, 71, 31))
        self.pushButton.clicked.connect(self.load)
        font = QtGui.QFont()
        font.setFamily("맑은 고딕")
        self.pushButton.setFont(font)
        self.pushButton.setAutoDefault(False)
        self.pushButton.setDefault(False)
        self.pushButton.setFlat(False)
        self.pushButton.setObjectName("pushButton")
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setGeometry(QtCore.QRect(0, 0, 270, 16))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setAlignment(QtCore.Qt.AlignCenter)
        self.progressBar.setFormat("")
        self.progressBar.setObjectName("progressBar")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 40, 31, 21))
        font = QtGui.QFont()
        font.setFamily("맑은 고딕")
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 60, 31, 21))
        font = QtGui.QFont()
        font.setFamily("맑은 고딕")
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(10, 80, 81, 21))
        font = QtGui.QFont()
        font.setFamily("맑은 고딕")
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(10, 200, 31, 21))
        font = QtGui.QFont()
        font.setFamily("맑은 고딕")
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(10, 220, 31, 21))
        font = QtGui.QFont()
        font.setFamily("맑은 고딕")
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        font = QtGui.QFont()
        font.setFamily("Consolas")
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(100, 80, 161, 121))
        self.listWidget.setObjectName("listWidget")
        self.listWidget.setFont(font)
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(40, 200, 211, 21))
        font = QtGui.QFont()
        font.setFamily("맑은 고딕")
        self.label_6.setFont(font)
        self.label_6.setOpenExternalLinks(True)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(40, 220, 211, 21))
        font = QtGui.QFont()
        font.setFamily("맑은 고딕")
        self.label_7.setFont(font)
        self.label_7.setOpenExternalLinks(True)
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(40, 40, 141, 21))
        font = QtGui.QFont()
        font.setFamily("맑은 고딕")
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(40, 60, 221, 21))
        font = QtGui.QFont()
        font.setFamily("맑은 고딕")
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(0, 31, 271, 21))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(10, 20, 250, 16))
        self.label_10.setScaledContents(True)
        self.label_10.setAlignment(QtCore.Qt.AlignCenter)
        self.label_10.setObjectName("label_10")
        MCInfo.setCentralWidget(self.centralwidget)

        self.retranslateUi(MCInfo)
        QtCore.QMetaObject.connectSlotsByName(MCInfo)

    def retranslateUi(self, MCInfo):
        _translate = QtCore.QCoreApplication.translate
        MCInfo.setWindowTitle(_translate("MCInfo", "MCInfo - Player"))
        self.textEdit.setPlaceholderText(_translate("MCInfo", "닉네임을 입력하십시오"))
        self.pushButton.setText(_translate("MCInfo", "정보 보기"))
        self.label.setText(_translate("MCInfo", "이름"))
        self.label_2.setText(_translate("MCInfo", "UUID"))
        self.label_3.setText(_translate("MCInfo", "이름 변경 기록"))
        self.label_4.setText(_translate("MCInfo", "스킨"))
        self.label_5.setText(_translate("MCInfo", "망토"))
        self.label_6.setText(_translate("MCInfo", "<a href=\"https://google.com\">스킨 링크</a>"))
        self.label_7.setText(_translate("MCInfo", "<a href=\"https://google.com\">망토 링크</a>"))
        self.label_8.setText(_translate("MCInfo", "이름 공간"))
        self.label_9.setText(_translate("MCInfo", "uuid 공간"))
        self.label_10.setText(_translate("MCInfo", "Made by Team-Fi"))

    def textChanged(self):
        if len(self.textEdit.text()) > 3:
            self.pushButton.setEnabled(True)
        else:
            self.pushButton.setEnabled(False)

    def load(self):
        self.listWidget.clear()
        with urllib.request.urlopen("https://api.mojang.com/users/profiles/minecraft/" + self.textEdit.text()) as url:
            nu = json.loads(url.read().decode())

        uuid = nu["id"]
        username = nu["name"]

        with urllib.request.urlopen("https://api.mojang.com/user/profiles/" + uuid + "/names") as url:
            nh = json.loads(url.read().decode())

        with urllib.request.urlopen("https://sessionserver.mojang.com/session/minecraft/profile/" + uuid) as url:
            pf = json.loads(base64.b64decode(json.loads(url.read().decode())["properties"][0]["value"]))

        for i in range(1, 101):
            import time
            time.sleep(0.01)
            self.progressBar.setValue(i)

        self.label_9.setText(uuid)
        self.label_8.setText(username)
        for val in nh:
            if "changedToAt" in val:
                self.listWidget.addItem(val["name"] + (" " * (17 - len(val["name"]))) + "(" + str(
                    datetime.datetime.utcfromtimestamp(val["changedToAt"] / 1000)) + ")")
            else:
                self.listWidget.addItem(val["name"])
        if "metadata" in pf["textures"]["SKIN"]:
            self.label_6.setText(f'<a href={pf["textures"]["SKIN"]["url"]}>스킨 링크 (슬림)</a>')
        else:
            self.label_6.setText(f'<a href={pf["textures"]["SKIN"]["url"]}>스킨 링크 (일반)</a>')
        if "CAPE" in pf["textures"]:
            self.label_7.setText(f'<a href={pf["textures"]["CAPE"]["url"]}>망토 링크</a>')
        else:
            self.label_7.setText('망토 없음')


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MCInfo = QtWidgets.QMainWindow()
    ui = Ui_MCInfo()
    ui.setupUi(MCInfo)
    MCInfo.show()
    app.exec_()
