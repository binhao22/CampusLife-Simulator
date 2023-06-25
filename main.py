import sys
from PyQt5 import QtGui, QtWidgets
from PyQt5.QtWidgets import*
from PyQt5.uic import*
import page as p
import eventcontroll as ev

# windowIcon
icon = QtGui.QIcon()
icon.addPixmap(QtGui.QPixmap("resource/images/icon.png"))
p.widget.setWindowIcon(icon)

# window框架大小
p.widget.setFixedHeight(600)
p.widget.setFixedWidth(900)



# show
p.widget.show()
p.app.exec_()

