from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon


class Ui_MCInfo(object):
    def setupUi(self, MCInfo):
        MCInfo.setObjectName("MCInfo")
        MCInfo.resize(530, 260)
        import os.path as path
        bundle_dir = getattr(sys, '_MEIPASS', path.abspath(path.dirname(__file__)))
        import os
        data_path = os.path.abspath(path.join(bundle_dir, 'icon.png'))
        MCInfo.setWindowIcon(QIcon(f"{data_path}"))
        self.centralwidget = QtWidgets.QWidget(MCInfo)
        self.centralwidget.setObjectName("centralwidget")
        self.textEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(10, 220, 171, 31))
        self.textEdit.textChanged[str].connect(self.textChanged)
        font = QtGui.QFont()
        font.setFamily("맑은 고딕")
        font.setPointSize(11)
        self.textEdit.setFont(font)
        self.textEdit.setObjectName("textEdit")

        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setEnabled(False)
        self.pushButton.setGeometry(QtCore.QRect(190, 220, 70, 30))
        font = QtGui.QFont()
        font.setFamily("맑은 고딕")
        self.pushButton.setFont(font)
        self.pushButton.setAutoDefault(False)
        self.pushButton.setDefault(False)
        self.pushButton.setFlat(False)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.load)
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setGeometry(QtCore.QRect(0, 0, 530, 16))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setAlignment(QtCore.Qt.AlignCenter)
        self.progressBar.setFormat("")
        self.progressBar.setObjectName("progressBar")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 40, 30, 20))
        font = QtGui.QFont()
        font.setFamily("맑은 고딕")
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 60, 40, 20))
        font = QtGui.QFont()
        font.setFamily("맑은 고딕")
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(10, 80, 60, 20))
        font = QtGui.QFont()
        font.setFamily("맑은 고딕")
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(10, 200, 30, 20))
        font = QtGui.QFont()
        font.setFamily("맑은 고딕")
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(270, 40, 70, 20))
        font = QtGui.QFont()
        font.setFamily("맑은 고딕")
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(80, 80, 180, 120))
        self.listWidget.setObjectName("listWidget")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(40, 200, 210, 20))
        font = QtGui.QFont()
        font.setFamily("맑은 고딕")
        self.label_6.setFont(font)
        self.label_6.setOpenExternalLinks(True)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(340, 40, 210, 20))
        font = QtGui.QFont()
        font.setFamily("맑은 고딕")
        self.label_7.setFont(font)
        self.label_7.setOpenExternalLinks(True)
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(40, 40, 140, 20))
        font = QtGui.QFont()
        font.setFamily("맑은 고딕")
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(50, 60, 210, 20))
        font = QtGui.QFont()
        font.setFamily("맑은 고딕")
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(0, 30, 530, 20))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(10, 20, 510, 20))
        self.label_10.setScaledContents(True)
        self.label_10.setAlignment(QtCore.Qt.AlignCenter)
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(270, 60, 70, 20))
        font = QtGui.QFont()
        font.setFamily("맑은 고딕")
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(340, 60, 210, 20))
        font = QtGui.QFont()
        font.setFamily("맑은 고딕")
        self.label_12.setFont(font)
        self.label_12.setOpenExternalLinks(True)
        self.label_12.setObjectName("label_12")
        self.listWidget_2 = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget_2.setGeometry(QtCore.QRect(340, 80, 180, 80))
        self.listWidget_2.setObjectName("listWidget_2")
        self.label_13 = QtWidgets.QLabel(self.centralwidget)
        self.label_13.setGeometry(QtCore.QRect(270, 80, 60, 20))
        font = QtGui.QFont()
        font.setFamily("맑은 고딕")
        self.label_13.setFont(font)
        self.label_13.setObjectName("label_13")
        self.listWidget_3 = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget_3.setGeometry(QtCore.QRect(340, 170, 180, 80))
        self.listWidget_3.setObjectName("listWidget_3")
        self.label_14 = QtWidgets.QLabel(self.centralwidget)
        self.label_14.setGeometry(QtCore.QRect(270, 170, 60, 20))
        font = QtGui.QFont()
        font.setFamily("맑은 고딕")
        self.label_14.setFont(font)
        self.label_14.setObjectName("label_14")
        MCInfo.setCentralWidget(self.centralwidget)
        self.actionPlayer = QtWidgets.QAction(MCInfo)
        self.actionPlayer.setObjectName("actionPlayer")
        self.actionServer = QtWidgets.QAction(MCInfo)
        self.actionServer.setObjectName("actionServer")

        self.retranslateUi(MCInfo)
        QtCore.QMetaObject.connectSlotsByName(MCInfo)

    def retranslateUi(self, MCInfo):
        _translate = QtCore.QCoreApplication.translate
        MCInfo.setWindowTitle(_translate("MCInfo", "MCInfo - Server"))
        self.textEdit.setPlaceholderText(_translate("MCInfo", "주소를 입력하십시오"))
        self.pushButton.setText(_translate("MCInfo", "정보 보기"))
        self.label.setText(_translate("MCInfo", "주소"))
        self.label_2.setText(_translate("MCInfo", "MOTD"))
        self.label_3.setText(_translate("MCInfo", "플레이어들"))
        self.label_4.setText(_translate("MCInfo", "버전"))
        self.label_5.setText(_translate("MCInfo", "호스트 이름"))
        self.label_6.setText(_translate("MCInfo", "서버가 오프라인임"))
        self.label_7.setText(_translate("MCInfo", "서버가 오프라인임"))
        self.label_8.setText(_translate("MCInfo", "서버가 오프라인임"))
        self.label_9.setText(_translate("MCInfo", "서버가 오프라인임"))
        self.label_10.setText(_translate("MCInfo", "Made by Team-Fi"))
        self.label_11.setText(_translate("MCInfo", "구동기 종류"))
        self.label_12.setText(_translate("MCInfo", "서버가 오프라인임"))
        self.label_13.setText(_translate("MCInfo", "플러그인들"))
        self.label_14.setText(_translate("MCInfo", "모드들"))
        self.actionPlayer.setText(_translate("MCInfo", "Player"))
        self.actionServer.setText(_translate("MCInfo", "Server"))

    def textChanged(self):
        if len(self.textEdit.text()) > 3:
            self.pushButton.setEnabled(True)
            self.retranslateUi(MCInfo)
        else:
            self.pushButton.setEnabled(False)

    def load(self):
        self.listWidget.clear()
        self.listWidget_2.clear()
        self.listWidget_3.clear()
        import urllib.request, json, ssl
        ssl._create_default_https_context = ssl._create_unverified_context

        address = self.textEdit.text()
        with urllib.request.urlopen("https://api.mcsrvstat.us/2/" + address) as url:
            info = json.loads(url.read().decode())

        for i in range(1, 101):
            import time
            time.sleep(0.01)
            self.progressBar.setValue(i)

        if info["online"]:
            self.label_8.setText(address)
            self.label_9.setText(info["motd"]["clean"][0])
            if "list" in info["players"]:
                self.label_3.setText(f'{info["players"]["online"]}<br>--------<br>{info["players"]["max"]}')
                [self.listWidget.addItem(x) for x in info["players"]["list"]]
            elif info["players"]["online"]:
                self.label_3.setText(f'{info["players"]["online"]}<br>--------<br>{info["players"]["max"]}')
            else:
                self.listWidget.clear()
            self.label_6.setText(info["version"])
            if "hostname" in info:
                self.label_7.setText(info["hostname"])
            else:
                self.label_7.setText("알 수 없음")
            if "software" in info:
                self.label_12.setText(info["software"])
            else:
                self.label_12.setText("알 수 없음")
            if "plugins" in info:
                [self.listWidget_2.addItem(x) for x in info["plugins"]["names"]]
            elif "mods" in info:
                [self.listWidget_3.addItem(x) for x in info["mods"]["names"]]


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MCInfo = QtWidgets.QMainWindow()
    ui = Ui_MCInfo()
    ui.setupUi(MCInfo)
    MCInfo.show()
    sys.exit(app.exec_())
