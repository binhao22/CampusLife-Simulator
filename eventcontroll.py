from PyQt5 import *
import sys
from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtWidgets import *
from PyQt5.uic import*
from PyQt5.QtCore import QObject
from PyQt5.QtCore import Qt, pyqtSignal
import createnode as node
from PyQt5 import QtCore
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import random
from py2neo import Graph,Node,Relationship,NodeMatcher
import page as p
class Controller(QObject):
    mySignal_1 = pyqtSignal(object)  # 创建信号，用于发送按钮已点击信号；
    mySignal_2 = pyqtSignal([str])  # 用于发送默认文件打开路径信号；信号有一个str类型的参数
    mySignal_3 = pyqtSignal(QLabel)
    labellist = []

    def __init__(self):
        i=0
        super(Controller, self).__init__()
        self.nodecreator= node.CreateNode("bolt://localhost:7687", "neo4j", "123456")
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.createlabel)
        self.eventlist1 = [p.Label, QWidget, QWidget, QWidget, p.Label, p.Label, p.Label, p.Label, p.Label, p.Label, p.Label]
        self.eventlist2 = [p.Label, QWidget, QWidget, QWidget, p.Label, p.Label, p.Label, p.Label, p.Label, p.Label, p.Label]
        self.eventlist3 = [QWidget, QWidget, QWidget, p.Label, p.Label, p.Label, p.Label, p.Label, p.Label, p.Label]
        self.eventlist4 = []
        self.eventlist5 = []
        self.eventlist5 = []
    def sendlabel(self,label):
        self.mySignal_3.emit(label)
    def createlabel(self):
            self.i=self.i+1
            if(self.i<3):
                 label = p.Label("test")
                 self.sendlabel().emit(label)
    def begin(self):
        self.timer.start(1000)

    def createlabel1(self, course):
        #获取节点信息
        list = []
        nodes_data = self.nodecreator.run("MATCH (n)-[:result]-(b) where n.name='"+course+"'return b.content").data()
        for node in nodes_data:
            labeltext = node['b.content']
            list.append(node['b.content'])
        i=random.randint(0,2)
        labeltext = "在"+course+"课上，你"+labeltext
        label = p.Label()
        label.setText(labeltext)






