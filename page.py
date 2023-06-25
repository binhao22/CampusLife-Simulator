import sys
from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtWidgets import*
from PyQt5.uic import*
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt, pyqtSignal,QTimer

class Page1(QWidget):
    singal1 = pyqtSignal([int])
    def __init__(self):
        super(Page1, self).__init__()
        loadUi("page1.ui", self)
        self.btn_start.clicked.connect(self.start)

    # 开始按钮
    def start(self):
        page2 = Page2()
        widget.insertWidget(1, page2)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def nextpage(self):
        self.singal1.emit(1)

class Page2(QWidget):
    singnal2 = pyqtSignal([int])
    def __init__(self):
        super(Page2, self).__init__()
        loadUi("page2.ui", self)
        self.btn_next.clicked.connect(self.nextpage)
        self.btn_prev.clicked.connect(self.prevpage)
        self.setIcon()
        self.btn_BIT.clicked.connect(self.setLabel_BIT)
        self.btn_history.clicked.connect(self.setLabel_history)
        self.btn_movie.clicked.connect(self.setLabel_movie)

    # 按钮高亮
    def setLabel_BIT(self):
        self.label_BIT.setStyleSheet("color: rgb(217, 150, 148);")
        self.label_history.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_movie.setStyleSheet("color: rgb(255, 255, 255);")

    def setLabel_history(self):
        self.label_history.setStyleSheet("color: rgb(217, 150, 148);")
        self.label_BIT.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_movie.setStyleSheet("color: rgb(255, 255, 255);")

    def setLabel_movie(self):
        self.label_movie.setStyleSheet("color: rgb(217, 150, 148);")
        self.label_BIT.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_history.setStyleSheet("color: rgb(255, 255, 255);")

    # 按钮Icon
    def setIcon(self):
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("resource/images/logo_BIT.png"))
        self.btn_BIT.setIcon(icon1)

        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("resource/images/logo_history.png"))
        self.btn_history.setIcon(icon2)

        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("resource/images/logo_movie.png"))
        self.btn_movie.setIcon(icon3)

    # 确认按钮
    def nextpage(self):
        global choice
        if(self.btn_BIT.isChecked()):
            choice = 1
        elif(self.btn_history.isChecked()):
            choice = 2
        elif(self.btn_movie.isChecked()):
            choice = 3
        page3 = Page3()
        widget.insertWidget(2, page3)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    # 返回按钮
    def prevpage(self):
        widget.setCurrentIndex(widget.currentIndex() - 1)


class Page3(QWidget):
    def __init__(self):
        super(Page3, self).__init__()
        loadUi("page3.ui", self)
        # 隐藏修改确认按钮
        self.btn_chk.setVisible(False)
        # 禁止编辑
        self.label_6.setFocusPolicy(QtCore.Qt.NoFocus)
        self.label_7.setFocusPolicy(QtCore.Qt.NoFocus)
        self.label_8.setFocusPolicy(QtCore.Qt.NoFocus)
        self.label_9.setFocusPolicy(QtCore.Qt.NoFocus)
        self.label_10.setFocusPolicy(QtCore.Qt.NoFocus)
        self.btn_next.clicked.connect(self.nextpage)
        self.btn_prev.clicked.connect(self.prevpage)
        self.setLabel()
        self.setIcon()
        self.btn_edit.clicked.connect(self.edit)
        self.btn_chk.clicked.connect(self.chk)

    # 修改按钮
    def edit(self):
        # 显示修改确认按钮
        self.btn_chk.setVisible(True)
        # 可编辑
        self.label_6.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.label_7.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.label_8.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.label_9.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.label_10.setFocusPolicy(QtCore.Qt.ClickFocus)
        # 编辑框设置
        self.label_6.setStyleSheet("background-color: rgb(60, 74, 110);\n"
                                   "border-radius: 5px;\n"
                                   "color: rgb(255, 255, 255);")
        self.label_7.setStyleSheet("background-color: rgb(60, 74, 110);\n"
                                   "border-radius: 5px;\n"
                                   "color: rgb(255, 255, 255);")
        self.label_8.setStyleSheet("background-color: rgb(60, 74, 110);\n"
                                   "border-radius: 5px;\n"
                                   "color: rgb(255, 255, 255);")
        self.label_9.setStyleSheet("background-color: rgb(60, 74, 110);\n"
                                   "border-radius: 5px;\n"
                                   "color: rgb(255, 255, 255);")
        self.label_10.setStyleSheet("background-color: rgb(60, 74, 110);\n"
                                    "border-radius: 5px;\n"
                                    "color: rgb(255, 255, 255);")

    # 修改确认按钮
    def chk(self):
        # 隐藏按钮
        self.btn_chk.setVisible(False)
        # 禁止编辑
        self.label_6.setFocusPolicy(QtCore.Qt.NoFocus)
        self.label_7.setFocusPolicy(QtCore.Qt.NoFocus)
        self.label_8.setFocusPolicy(QtCore.Qt.NoFocus)
        self.label_9.setFocusPolicy(QtCore.Qt.NoFocus)
        self.label_10.setFocusPolicy(QtCore.Qt.NoFocus)
        # 恢复原样子
        self.label_6.setStyleSheet("background-color: rgb(51, 63, 80);\n"
                                   "border: 0px;\n"
                                   "color: rgb(255, 255, 255);")
        self.label_7.setStyleSheet("background-color: rgb(51, 63, 80);\n"
                                   "border: 0px;\n"
                                   "color: rgb(255, 255, 255);")
        self.label_8.setStyleSheet("background-color: rgb(51, 63, 80);\n"
                                   "border: 0px;\n"
                                   "color: rgb(255, 255, 255);")
        self.label_9.setStyleSheet("background-color: rgb(51, 63, 80);\n"
                                   "border: 0px;\n"
                                   "color: rgb(255, 255, 255);")
        self.label_10.setStyleSheet("background-color: rgb(51, 63, 80);\n"
                                    "border: 0px;\n"
                                    "color: rgb(255, 255, 255);")

    # profile数据
    def setLabel(self):
        if (choice == 1):
            self.label_topic.setText("恭喜你来到了北京理工大学!")
            self.label_topic2.setText("请核对您的学籍信息:")
            self.label_1.setText("姓名：")
            self.label_2.setText("姓别：")
            self.label_3.setText("籍贯：")
            self.label_4.setText("学号：")
            self.label_5.setText("专业：")
            self.label_6.setText("工人")
            self.label_7.setText("男")
            self.label_8.setText("北京")
            self.label_9.setText("1120219999")
            self.label_10.setText("信息科学技术")
        elif (choice == 2):
            self.label_topic.setText("2")
        elif (choice == 3):
            self.label_topic.setText("3")

    # TopicIcon
    def setIcon(self):
        if (choice == 1):
            self.logo.setPixmap(QtGui.QPixmap("resource/images/logo_BIT.png"))
            self.logo2.setPixmap(QtGui.QPixmap(
                "resource/images/profile_BIT.png"))
        elif (choice == 2):
            self.logo.setPixmap(QtGui.QPixmap(
                "resource/images/logo_history.png"))
        elif (choice == 3):
            self.logo.setPixmap(QtGui.QPixmap(
                "resource/images/logo_movie.png"))

    # 确认按钮
    def nextpage(self):
        # 保存用户输入的数据 name、gender、etc
        global key_1, key_2, key_3
        key_1 = self.label_6.toPlainText()
        key_2 = self.label_7.toPlainText()
        key_3 = self.label_10.toPlainText()

        page4 = Page4()
        widget.insertWidget(3, page4)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    # 返回按钮
    def prevpage(self):
        widget.setCurrentIndex(widget.currentIndex() - 1)


class Page4(QWidget):
    signal1 = pyqtSignal()
    def __init__(self):
        super(Page4, self).__init__()
        loadUi("page4.ui", self)
        self.btn_next.clicked.connect(self.nextpage)
        self.btn_prev.clicked.connect(self.prevpage)
        self.btn_refresh.clicked.connect(self.refresh)
        self.setLabel()
        self.setIcon()

    # 体检数据
    def setLabel(self):
        if (choice == 1):
            self.label_topic.setText("你拿到了入学时的体检报告：")
            self.key_1.setText("姓名：")
            self.key_2.setText("姓别：")
            self.key_3.setText("专业：")
            self.key_4.setText("身高：")
            self.key_5.setText("体重：")
            self.key_6.setText("资产：")
            self.key_7.setText("体质：")
            self.key_8.setText("智力：")
            self.key_9.setText("魅力：")
            self.key_10.setText("能力：")
            self.key_11.setText("学分：")
            self.key_12.setText("爱好：")
            # 用户输入的数据
            self.value_1.setText(key_1)
            self.value_2.setText(key_2)
            self.value_3.setText(key_3)
            self.value_4.setText("？")
            self.value_5.setText("？")
            self.value_6.setText("？")
            self.value_7.setText("？")
            self.value_8.setText("？")
            self.value_9.setText("？")
            self.value_10.setText("？")
            self.value_11.setText("？")
            self.value_12.setText("？")
        elif (choice == 2):
            self.label_topic.setText("2")
        elif (choice == 3):
            self.label_topic.setText("3")

    # TopicIcon
    def setIcon(self):
        if (choice == 1):
            self.logo.setPixmap(QtGui.QPixmap("resource/images/logo_BIT.png"))
        elif (choice == 2):
            self.logo.setPixmap(QtGui.QPixmap(
                "resource/images/logo_history.png"))
        elif (choice == 3):
            self.logo.setPixmap(QtGui.QPixmap(
                "resource/images/logo_movie.png"))

    # 再体检一次按钮
    def refresh(self):
        pass

    # 确认按钮
    def nextpage(self):
        if (choice == 1):
            page5 = Page5()
            widget.insertWidget(4, page5)
            widget.setCurrentIndex(widget.currentIndex() + 1)
            self.setVisible(False)
            self.signal1.emit()
        if (choice == 2):
            pass
        if (choice == 3):
            pass

    # 返回按钮
    def prevpage(self):
        widget.setCurrentIndex(widget.currentIndex() - 1)


# BIT事件
class Page5(QWidget):
    signal1 = pyqtSignal()
    vlayout = QVBoxLayout()

    def __init__(self):
        super(Page5, self).__init__()
        loadUi("page5.ui", self)
        self.flag =0
        # 翻页按钮
        self.btn_next_1.clicked.connect(self.nextpage_1)
        # 选择事件按钮
        self.setbutton()
        self.setLabel()
        self.setIcon()
        self.btn_stats.clicked.connect(self.stats)
        # 隐藏事件框架
        self.episode_2.setVisible(False)
        self.episode_1.setVisible(False)
        self.stackedWidget.setVisible(False)
        # self.episode_3.setVisible(False)
        # self.episode_4.setVisible(False)
        # self.episode_5.setVisible(False)
        # self.episode_6.setVisible(False)
        itemlist = []
        self.layout = QVBoxLayout()
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.showw)
        self.timer1 = QTimer(self)
        self.timer1.timeout.connect(self.showl)
        self.timer.start(1000)
        self.labelwidget= QWidget(self)
        self.labelwidget.setStyleSheet("background-color: rgb(51,63,80)")
        self.labelwidget.setGeometry(35, 190, 820, 300)
        self.labelwidget.lower()

        # label = QLabel()
        # label.setText("   "+"九月中旬：在经历了两门课九月中旬选到了两旬选到了两旬选到了两旬选到了两旬选在经历了两门课九月中旬选到了两旬选到了两旬选到了两旬选到了两旬选到了两旬选到了两旬选到了门课到了两旬选到了两旬选到了门课")
        # label.setStyleSheet("color:white; font-size: 25px;font-family:Microsoft YaHei")
        # label.setWordWrap(True)
        # label.setMinimumWidth(800)
        # label.setMaximumWidth(800)
        # label.setAutoFillBackground(True)
        # label1 = QLabel()
        # label1.setText(
        #     "   " + "ddddddddddddddddddddddddddddddddddddddddddddddddd")
        # label1.setStyleSheet("font-size:20px")
        # label1.setWordWrap(True)
        # label1.setMinimumWidth(800)
        # label1.setMaximumWidth(800)
        # label1.setAutoFillBackground(True)
        # # layout.addWidget(label)
        # # layout.addWidget(label1)
        # label13= Label()
        # label13.setText("两旬选到两旬选到两旬选到两旬选到两旬选到两旬选到两旬选到两旬选到两旬选到两旬选到两旬选到两旬选到两旬选到两旬选到两旬选到两旬选到两旬选到了两旬选到了两旬选在经")
        # label13.resize(810, label13.getheight())
        # self.layout.addWidget(label13)
        # self.labelwidget.resize(820, label13.getheight())
        # labelwidget.setGeometry(40, 200, 805, label1.height()+10)
        # self.labelwidget.setLayout(self.layout)
        # print(label13.height())
        # print(self.labelwidget.height())
    def showw(self):
        self.episode_1.setVisible(True)

        self.timer1.start(1000)
    def showl(self):
        if(self.flag ==0):
            self.stackedWidget.setVisible(True)
    def slot(self,a):
        self.episode_3.setText(a)
    # 可选事件按钮
    def setbutton(self):
        self.btn_physical = [self.btn_physical_0, self.btn_physical_1, self.btn_physical_2,
                             self.btn_physical_3, self.btn_physical_4, self.btn_physical_5]
        tmp = 0
        for i in physical:
            self.btn_physical[tmp].setText("%s" % i)
            tmp += 1

    # 往通识课选课page
    def nextpage_1(self):
        global event_2
        if (self.btn_physical_0.isChecked()):
            event_2 = physical[0]
        if (self.btn_physical_1.isChecked()):
            event_2 = physical[1]
        if (self.btn_physical_2.isChecked()):
            event_2 = physical[2]
        else:
            pass
    # 可选事件内容
        self.episode_2.setText("九月中旬：在经历看脸的抽签选课后，你共选到了1门课：体育课——" + '<font color="#dee830" > %s < /font >' %
                               event_2)
        # self.stackedWidget.setCurrentIndex(
        #     self.stackedWidget.currentIndex() + 1)
        self.episode_2.setVisible(True)
        self.stackedWidget.setVisible(False)
        self.flag =1
    # 随机事件内容
    def setLabel(self):
        self.episode_1.setText(
            "九月上旬：" + '<font color="#dee830" > %s < /font >' % event_1[0] + '<font color="#2afa4c" > %s < /font >' % event_1_2[0])

    # TopicIcon
    def setIcon(self):
        self.logo.setPixmap(QtGui.QPixmap("resource/images/logo_BIT.png"))

    # 查看属性按钮
    def stats(self):
        pass

    def getlabel(self,label):
        text = self.text()
        length = len(text)
        height = int(length / 40)
        height = 30 * height
        height = height+ self.labelwidget.height()
        self.labelwidget.setMinimumHeight(height)
        self.layout.addWidget(label)

    def slot(self):
        self.show()

class Label(QLabel):
    def __init__(self):
        super(Label, self).__init__()
        self.setStyleSheet("color:white; font-size: 20px;font-family:楷体; background:rgb(114,97,127); border-radius: 5px")

        self.setWordWrap(True)
        self.setMinimumWidth(800)
        self.setMaximumWidth(800)
    def getheight(self):
        text = self.text()
        length = len(text)
        height = int(length/40)
        height = 30*height+50
        print(text)
        return height

# Topic变量
choice = 0  # 选择模式
key_1 = ""  # 用户输入的数据
key_2 = ""
key_3 = ""
# 随机事件变量
event_1 = ["烈日炎炎，英姿飒爽，你标准的站姿获得教官的夸赞"]
event_1_2 = ["，体质+2，魅力+2"]
# 可选事件变量
physical = ["篮球（张长礼）", "野外生存（朱峰）", "网球（王勇）"]


# main
app = QApplication(sys.argv)
widget = QtWidgets.QStackedWidget()
page1 = Page1()
widget.insertWidget(0, page1)

