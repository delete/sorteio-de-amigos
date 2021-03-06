# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'interface.ui'
#
# Created: Tue Apr  2 18:18:07 2013
#      by: PyQt4 UI code generator 4.9.1
# Versão 1.2

##############################
#
#Mudar a cada 1h
#Pegar no site, https://developers.facebook.com/docs/reference/api/examples/
#Connections -> Friends     
#Mudar no arquivo url
#
###############################

from PyQt4 import QtCore, QtGui
from PyQt4.QtCore import *
import sys
import os
import random
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
        Dialog.setWindowIcon(QtGui.QIcon('icon.ico'))
        
        #Sortear
        self.pushButton = QtGui.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(110, 300, 99, 24))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))        
        QtCore.QObject.connect(self.pushButton, QtCore.SIGNAL("clicked()"), self.atividade)        

        #Nome da pessoa
        self.label = QtGui.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(40, 260, 231, 20))
        self.label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName(_fromUtf8("label"))

        self.label2 = QtGui.QLabel(Dialog)
        self.label2.setGeometry(QtCore.QRect(206, 320, 101, 20))
        self.label2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label2.setAlignment(QtCore.Qt.AlignCenter)
        self.label2.setObjectName(_fromUtf8("label2"))
        QtCore.QObject.connect(self.label2, QtCore.SIGNAL("linkActivated(QString)"), self.openUrl) 


        self.image = QtGui.QLabel(Dialog)
        self.image.setPixmap(QtGui.QPixmap('images/fb-icon.png')) # imagem default      
        self.image.setGeometry(60, 30, 200, 200) 

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtGui.QApplication.translate("Dialog", "Sorteio de Amigos", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton.setText(QtGui.QApplication.translate("Dialog", "Sortear", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Dialog","Que os sorteios comecem!" , None, QtGui.QApplication.UnicodeUTF8))
        self.label2.setText(QtGui.QApplication.translate("Dialog", '<a href="http://www.twitter.com/pinheirofellipe">Contato</a></em>', None, QtGui.QApplication.UnicodeUTF8))

    def atividade(self):    
        #Deleta as fotos, se tiverem mais de 10
        Facebook.limpaDados()

        #Sorteia uma pessoa        
        sorteado = random.choice(lista)

        #Intancia um objeto com o vencedor        
        f = Facebook(sorteado)

        #Procura o nome pelo id
        data = f.procura()    

        #Baixa a foto do perfil
        arq = f.baixarFoto()

        #Deleta o sorteado da lista        
        lista.remove(sorteado)

        #Muda os dados do sorteado na janela
        #self.label.setText(QtGui.QApplication.translate("Dialog",'<a href="http://www.gogole.com.br>' +  data ['name'] +'</a></em>', None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Dialog",'<a href="http://www.facebook.com.br/'+ data['id'] +'">'+ data['name'] +'</a></em>', None, QtGui.QApplication.UnicodeUTF8))
        QtCore.QObject.connect(self.label, QtCore.SIGNAL("linkActivated(QString)"), self.openUrl) 
        self.image.setPixmap(QtGui.QPixmap(arq))

    def openUrl(self,URL):
        QtGui.QDesktopServices().openUrl(QUrl(URL))

        

#Janela de erro
class Error(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))        
        Dialog.resize(400, 245)
        Dialog.setMaximumSize(QtCore.QSize(400, 245))
        Dialog.setWindowIcon(QtGui.QIcon('icon.ico'))

        self.label = QtGui.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(120, 10, 181, 20))
        self.label.setObjectName(_fromUtf8("label"))

        self.label2 = QtGui.QLabel(Dialog)
        self.label2.setGeometry(QtCore.QRect(50, 40, 301, 31))
        self.label2.setObjectName(_fromUtf8("label2"))
        QtCore.QObject.connect(self.label2, QtCore.SIGNAL("linkActivated(QString)"), self.openUrl) 
        
        self.label3 = QtGui.QLabel(Dialog)
        self.label3.setGeometry(QtCore.QRect(80, 70, 241, 31))
        self.label3.setObjectName(_fromUtf8("label3"))
        
        #Contato
        self.label4 = QtGui.QLabel(Dialog)
        self.label4.setGeometry(QtCore.QRect(340, 220, 56, 15))
        self.label4.setObjectName(_fromUtf8("label4"))
        QtCore.QObject.connect(self.label4, QtCore.SIGNAL("linkActivated(QString)"), self.openUrl) 

        #Botão sair
        self.pushButton = QtGui.QPushButton(Dialog) 
        self.pushButton.setGeometry(QtCore.QRect(250, 190, 99, 24))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        
        #Botão atualizar
        self.pushButton2 = QtGui.QPushButton(Dialog) 
        self.pushButton2.setGeometry(QtCore.QRect(40, 190, 99, 24))
        self.pushButton2.setObjectName(_fromUtf8("pushButton2"))

        self.textEdit = QtGui.QTextEdit(Dialog)        
        self.textEdit.setGeometry(QtCore.QRect(10, 110, 371, 51))
        self.textEdit.setObjectName(_fromUtf8("textEdit"))

        QtCore.QObject.connect(self.pushButton, QtCore.SIGNAL("clicked()"), self.sair)
        QtCore.QObject.connect(self.pushButton2, QtCore.SIGNAL("clicked()"), self.atualizar)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):        
        Dialog.setWindowTitle(QtGui.QApplication.translate("Dialog", "ERROR", None, QtGui.QApplication.UnicodeUTF8))        
        self.label.setText(QtGui.QApplication.translate("Dialog", "Token do Facebook expirou.", None, QtGui.QApplication.UnicodeUTF8))
        self.label2.setText(QtGui.QApplication.translate("Dialog", 'Copie a URL de: "Connections -> Friends" nesse' + '<a href="https://developers.facebook.com/docs/reference/api/examples/"> link.</a></em>', None, QtGui.QApplication.UnicodeUTF8))
        self.label3.setText(QtGui.QApplication.translate("Dialog", "Cole a URL, atualize e reabra o programa.", None, QtGui.QApplication.UnicodeUTF8))    
        self.label4.setText(QtGui.QApplication.translate("Dialog", '<a href="http://www.twitter.com/pinheirofellipe">Contato</a></em>', None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton.setText(QtGui.QApplication.translate("Dialog", "Sair", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton2.setText(QtGui.QApplication.translate("Dialog", "Atualizar", None, QtGui.QApplication.UnicodeUTF8))
        self.textEdit.setText(QtGui.QApplication.translate("Dialog", "", None, QtGui.QApplication.UnicodeUTF8))

    def sair(self):
        sys.exit()

    def atualizar(self):
        url = self.textEdit.toPlainText()
        arq = open("url.txt", "w")
        arq.write(url)
        arq.close()                
        self.sair()

    def openUrl(self,URL):
        QtGui.QDesktopServices().openUrl(QUrl(URL))

def carregarUrl():    
    arq = open("url.txt", "r")
    url = arq.read()
    arq.close()            
    return url


if __name__ == "__main__":
    
    try:
        url = carregarUrl()
        lista,quantidade = Facebook.listarAmigos(url,'id')    
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