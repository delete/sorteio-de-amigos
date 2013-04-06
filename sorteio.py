# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'interface.ui'
#
# Created: Tue Apr  2 18:18:07 2013
#      by: PyQt4 UI code generator 4.9.1
# Versão 2.0

##############################
#
#Mudar a cada 1h
#Pegar no site, https://developers.facebook.com/docs/reference/api/examples/
#Connections -> Friends     
#Mudar no arquivo url
#
###############################

from PyQt4 import QtCore, QtGui
import sys
import os
from random import randint
from fbk import Facebook #arquivo fbk.py


try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s


#Janela principal
class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(320, 345)    
        Dialog.setMaximumSize(QtCore.QSize(320, 345))
        self.pushButton = QtGui.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(110, 300, 99, 24))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))        
        QtCore.QObject.connect(self.pushButton, QtCore.SIGNAL("clicked()"), self.atividade)

        #Nome da pessoa
        self.label = QtGui.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(20, 260, 231, 20))
        self.label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName(_fromUtf8("label"))

        self.label2 = QtGui.QLabel(Dialog)
        self.label2.setGeometry(QtCore.QRect(206, 320, 101, 20))
        self.label2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label2.setAlignment(QtCore.Qt.AlignCenter)
        self.label2.setObjectName(_fromUtf8("label2"))        


        self.image = QtGui.QLabel(Dialog)
        self.image.setPixmap(QtGui.QPixmap('images/fb-icon.png')) # imagem default      
        self.image.setGeometry(69, 20, 211, 200)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtGui.QApplication.translate("Dialog", "Sorteio de Amigos", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton.setText(QtGui.QApplication.translate("Dialog", "Sortear", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Dialog", "Que comecem os sorteios.", None, QtGui.QApplication.UnicodeUTF8))
        self.label2.setText(QtGui.QApplication.translate("Dialog", "@pinheirofellipe", None, QtGui.QApplication.UnicodeUTF8))

    def atividade(self):    
        #Deleta as fotos, se tiver mais de 10
        Facebook.limpaDados()

        #Sorteia um numero
        sorteado = sorteia(lista, cont)

        #Intancia um objeto com o vencedor
        f = Facebook(lista[sorteado])


        #procura o nome pelo id
        data = f.procura()    

        arq = f.baixarFoto()

        #deleta o sorteado da lista
        lista.pop(sorteado)

        #Muda os dados dos sorteados
        self.label.setText(QtGui.QApplication.translate("Dialog",data['name'], None, QtGui.QApplication.UnicodeUTF8))
        self.image.setPixmap(QtGui.QPixmap(arq))

#Janela de erro
class Error(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        #Dialog.resize(250, 194)
        Dialog.resize(345, 345)

        self.label = QtGui.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(40, 20, 181, 20))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(30, 60, 221, 31))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        
        #Botão sair
        self.pushButton = QtGui.QPushButton(Dialog) 
        self.pushButton.setGeometry(QtCore.QRect(130, 160, 99, 24))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        
        #Botão atualizar
        self.pushButton2 = QtGui.QPushButton(Dialog) 
        self.pushButton2.setGeometry(QtCore.QRect(10, 160, 99, 24))
        self.pushButton2.setObjectName(_fromUtf8("pushButton2"))

        self.textEdit = QtGui.QTextEdit(Dialog)
        self.textEdit.setGeometry(QtCore.QRect(10, 110, 231, 31))
        self.textEdit.setObjectName(_fromUtf8("textEdit"))

        QtCore.QObject.connect(self.pushButton, QtCore.SIGNAL("clicked()"), self.sair)
        QtCore.QObject.connect(self.pushButton2, QtCore.SIGNAL("clicked()"), self.atualizar)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        
        Dialog.setWindowTitle(QtGui.QApplication.translate("Dialog", "ERROR", None, QtGui.QApplication.UnicodeUTF8))        
        self.label.setText(QtGui.QApplication.translate("Dialog", "Token do Facebook expirou.", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("Dialog", "Por favor, atualize o link \ne reabra o programa.", None, QtGui.QApplication.UnicodeUTF8))    
        self.pushButton.setText(QtGui.QApplication.translate("Dialog", "Sair", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton2.setText(QtGui.QApplication.translate("Dialog", "Atualizar", None, QtGui.QApplication.UnicodeUTF8))
        self.textEdit.setText(QtGui.QApplication.translate("Dialog", "", None, QtGui.QApplication.UnicodeUTF8))

    def sair(self):
        sys.exit()

    def atualizar(self):
        url = self.textEdit.toPlainText()
        arq = open("url", "w")
        arq.write(url)
        arq.close()                
        self.sair()


def sorteia(lista, cont):
    lista.sort()
    sorteado = randint(0,cont)
    return sorteado


def carregarUrl():
    arq = open("url", "r")
    url = arq.read()
    arq.close()
    return url


def main():
    try:
        url = carregarUrl()
        lista,cont = Facebook.listarAmigos(url,'id')        
        
    except Exception: #abre a janela de erro
        app = QtGui.QApplication(sys.argv)
        error = QtGui.QDialog()
        ui = Error()
        ui.setupUi(error)
        error.show()
        sys.exit(app.exec_())
    else:
        app = QtGui.QApplication(sys.argv)
        Dialog = QtGui.QDialog()
        ui = Ui_Dialog()
        ui.setupUi(Dialog)
        Dialog.show()
        sys.exit(app.exec_())

if __name__ == "__main__":
    
    main()