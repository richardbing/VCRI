# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'vcri.ui'
#
# Created: Fri Jun 23 12:24:33 2017
#      by: PyQt4 UI code generator 4.10
#
# WARNING! All changes made in this file will be lost!

import os, sys
from PyQt4 import QtCore, QtGui
from PyQt4.QtGui import QFont as font
from main import vcri
from main import checkPath, searchSRSfile

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_vcri(object):
    def __init__(self, *args, **kwargs):
        self.paths = []
        self.protocolPath = ''
        self.srsPath = ''
        self.stage = []
        return super(Ui_vcri, self).__init__(*args, **kwargs)

    def setupUi(self, vcriUi):
        vcriUi.setObjectName(_fromUtf8("vcriUi"))
        vcriUi.setEnabled(True)
        vcriUi.resize(845, 543)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(vcriUi.sizePolicy().hasHeightForWidth())
        vcriUi.setSizePolicy(sizePolicy)
        self.gridLayout_3 = QtGui.QGridLayout(vcriUi)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.tabWidget = QtGui.QTabWidget(vcriUi)
        self.tabWidget.setEnabled(True)
        self.tabWidget.setTabPosition(QtGui.QTabWidget.North)
        self.tabWidget.setTabShape(QtGui.QTabWidget.Rounded)
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.Menu = QtGui.QWidget()
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Menu.sizePolicy().hasHeightForWidth())
        self.Menu.setSizePolicy(sizePolicy)
        self.Menu.setObjectName(_fromUtf8("Menu"))
        self.gridLayout = QtGui.QGridLayout(self.Menu)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.label = QtGui.QLabel(self.Menu)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        
        
        # menu label
        self.label.setSizePolicy(sizePolicy)
        self.label.setText("Type or copy/paste the protocols folder path.")
        self.label.setObjectName(_fromUtf8("label"))


        self.verticalLayout.addWidget(self.label)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.lineEdit = QtGui.QLineEdit(self.Menu)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit.sizePolicy().hasHeightForWidth())
        self.lineEdit.setSizePolicy(sizePolicy)
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.horizontalLayout.addWidget(self.lineEdit)
      
        
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 1, 0, 1, 1)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
       
        # Search button
        self.pushButton = QtGui.QPushButton(self.Menu)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.horizontalLayout.addWidget(self.pushButton)
        
        # OK button 
        self.pushButton_2 = QtGui.QPushButton(self.Menu)
        self.pushButton_2.setCheckable(False)               
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.horizontalLayout_2.addWidget(self.pushButton_2)
        
        # Cancel button
        self.pushButton_3 = QtGui.QPushButton(self.Menu)
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.horizontalLayout_2.addWidget(self.pushButton_3)
        
        
        self.gridLayout.addLayout(self.horizontalLayout_2, 2, 0, 1, 1)
        self.tabWidget.addTab(self.Menu, _fromUtf8(""))
        
        
        self.Textview = QtGui.QWidget()
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Textview.sizePolicy().hasHeightForWidth())
        self.Textview.setSizePolicy(sizePolicy)
        self.Textview.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.Textview.setObjectName(_fromUtf8("Textview"))
        self.gridLayout_2 = QtGui.QGridLayout(self.Textview)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))

        #self.label_2 = QtGui.QLabel(self.Textview)
        self.text = QtGui.QPlainTextEdit()
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.text.sizePolicy().hasHeightForWidth())
        self.text.setSizePolicy(sizePolicy)
        #self.text.setText(_fromUtf8(""))
        self.text.setObjectName(_fromUtf8("text"))
        self.verticalLayout_2.addWidget(self.text)

        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        spacerItem2 = QtGui.QSpacerItem(376, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem2)
        self.pushButton_4 = QtGui.QPushButton(self.Textview)
        
        # Save button
        self.pushButton_4.setObjectName(_fromUtf8("pushButton_4"))
        self.horizontalLayout_3.addWidget(self.pushButton_4)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.gridLayout_2.addLayout(self.verticalLayout_2, 0, 0, 1, 1)
        self.tabWidget.addTab(self.Textview, _fromUtf8(""))
        self.gridLayout_3.addWidget(self.tabWidget, 0, 0, 1, 1)

        self.retranslateUi(vcriUi)
        self.tabWidget.setCurrentIndex(0)

        
     
        QtCore.QObject.connect(self.pushButton, QtCore.SIGNAL(_fromUtf8("clicked()")), self.singleBrowse)
        QtCore.QObject.connect(self.pushButton_2, QtCore.SIGNAL(_fromUtf8("clicked()")), self.getPath)
        QtCore.QObject.connect(self.pushButton_3, QtCore.SIGNAL(_fromUtf8("clicked()")), self.deletePath)
        #QtCore.QObject.connect(self.pushButton_3, QtCore.SIGNAL(_fromUtf8("clicked()")), self.label.clear)
        #QtCore.QObject.connect(self.lineEdit, QtCore.SIGNAL(_fromUtf8("textChanged(QString)")), self.label.setText(self.lineEdit.text()))
        QtCore.QMetaObject.connectSlotsByName(vcriUi)

    def retranslateUi(self, vcriUi):
        vcriUi.setWindowTitle(_translate("vcrrUi", "VCRI", None))
        self.pushButton.setText(_translate("vcriUi", "Search", None))
        self.pushButton_2.setText(_translate("vcriUi", "OK", None))
        self.pushButton_3.setText(_translate("vcriUi", "Cancel", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Menu), _translate("vcriUi", "Menu", None))
        self.pushButton_4.setText(_translate("vcriUi", "Save", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Textview), _translate("vcriUi", "Textview", None))

    def delay(self, time):
        count = 0
        while 1:
            count += 1
            if count == time:
                return

    def singleBrowse(self):
        #filePaths = QtGui.QFileDialog.getOpenFileNames()
        filePaths = QtGui.QFileDialog.getExistingDirectory()
        self.lineEdit.setText(filePaths)
    
    def processDoc(self):
        doc = vcri(self.srsPath, self.protocolPath)
        from DOCX_Creator import DocxWrite, Document
        doc.writeFile()
        doc.writeSrsRequirementFlie()
        doc.writeSystemRequirementFlie()
        doc.writeTextStringFlie()
        return True

    def stageInit(self, protocolPath, srsPath, paths):
        self.protocolPath = protocolPath
        self.srsPath = srsPath
        self.paths = paths
        self.lineEdit.clear()
        self.label.setText("Type or copy/paste the protocols folder path.")
    def stageOne(self, protocolPath, srsPath, paths):
        self.protocolPath = protocolPath
        self.srsPath = srsPath
        self.paths = paths
        self.lineEdit.clear()
        self.label.setText("Type or copy/paste the SRS folder path.")
    def stageThree(self, protocolPath, srsPath, paths):
        self.protocolPath = protocolPath
        self.srsPath = srsPath
        self.paths = paths
        self.lineEdit.clear()
        self.label.setText("In process please wait......")
    def stageTwo(self, protocolPath, srsPath, paths):
        self.protocolPath = protocolPath
        self.srsPath = srsPath
        self.paths = paths
        self.lineEdit.clear()
        self.label.setText("In process please wait......")
    def displayText(self):
        t=open('vcri.txt').read()
        self.text.setPlainText(t)

    
    def loadPath(self):
        if len(self.paths) == 1:
            self.protocolPath = os.path.join(str(self.paths[0]))
            self.label.setText("Type or copy/paste the SRS folder path.")
            self.lineEdit.clear()
        elif len(self.paths) == 2:
            temp = searchSRSfile(str(self.paths[1]))
            if temp:
                self.srsPath = os.path.join(str(self.paths[1]), temp)
                self.label.setText("In process please wait......")
                self.label.repaint()
                self.lineEdit.clear()
                self.lineEdit.repaint()
                if self.processDoc():
                    self.label.setText("File created in the current folder as vcri.txt")
                    self.displayText()
                else:
                    self.label.setText("Please check the target files in the folder")
            else:
                self.label.setText("No SRS document in target folder. please type or copy/paste the SRS folder path again.")
        elif len(self.paths) == 0:
            self.init()
            self.label.setText("Type or copy/paste the protocols folder path.")

    def deletePath(self):
        self.lineEdit.clear()
        if len(self.paths) == 2:
            self.paths.remove(self.paths[1])
            self.label.setText("Type or copy/paste the SRS folder path.")
            self.lineEdit.setText(str(self.srsPath))
        elif len(self.paths) == 1:
            self.paths.remove(self.paths[0])
            self.label.setText("Type or copy/paste the protocols folder path.")
            self.lineEdit.setText(str(self.protocolPath))
            
        
    def getPath(self):
        if self.lineEdit.text():
            self.paths.append(self.lineEdit.text())
            self.loadPath()



def main():
    app = QtGui.QApplication(sys.argv)
    vcriUi = QtGui.QWidget()
    ui = Ui_vcri()
    ui.setupUi(vcriUi)
    vcriUi.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()

