from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5 import QtWidgets as QtW
from BusquedasInView.Estructuras.Binario import Binario

from BusquedasInView.Estructuras.EstructuraInterna import EstructuraInterna
from BusquedasInView.Estructuras.Secuencial import Secuencial


from CamposView.Campos import Campos
class BusquedasInView(QGroupBox):
    def __init__(self, p:QWidget):
        super().__init__(p)

        # variable para la informacion
        self.campos=Campos()
        #variables logicas
        self.estructura:EstructuraInterna = None
        self.datoBuscado : int = None

        self.setStyleSheet("background-color:#DECCA6")

        self.tabla = QTableWidget(self)
        self.tabla.setColumnCount(1)
        self.tabla.setHorizontalHeaderLabels(["Valor"])
        self.tabla.setGeometry(880, 20, 170, 650)
        self.tabla.horizontalScrollBar().setVisible(False)
        self.tabla.setColumnWidth(0, 140)
        self.tabla.setStyleSheet("QTableWidget{border:1px solid black; background-color:#EBE6D2}")

        panelEstructura = QGroupBox(self)
        panelEstructura.setGeometry(10,20,860,320)
        panelEstructura.setStyleSheet("QGroupBox{border:1px solid black}")

        label = QLabel("Creacion Estructura",panelEstructura)
        label.move(120,60)

        #seccion de entradas
        label = QLabel("Tipo de Busqueda",self)
        label.move(105,125)
        label.setFont(QFont("Arial",9,QFont.Bold))
        self.opcionTipoBusq = QComboBox(self)
        self.opcionTipoBusq.addItems(["Secuencial","Binaria"])
        self.opcionTipoBusq.move(220,120)
        self.opcionTipoBusq.resize(120,30)
        self.opcionTipoBusq.setFont(QFont("Arial",9,QFont.Bold))
        self.opcionTipoBusq.currentTextChanged.connect(self.deshabilitar)
        self.opcionTipoBusq.setStyleSheet("background-color:#EBE6D2")

        label = QLabel("Rango",self)
        label.move(345,125)
        label.setFont(QFont("Arial",9,QFont.Bold))
        self.campoRango = QTextEdit(self)
        self.campoRango.setFrameStyle(1)
        self.campoRango.move(390,120)
        self.campoRango.resize(80,30)
        self.campoRango.setFont(QFont("Arial",9))
        self.campoRango.setStyleSheet("background-color:#EBE6D2")

        label = QLabel("Digitos Clave",self)
        label.move(475,125)
        label.setFont(QFont("Arial",9,QFont.Bold))
        self.campoDigitos = QTextEdit(self)
        self.campoDigitos.setFrameStyle(1)
        self.campoDigitos.move(550,120)
        self.campoDigitos.resize(80,30)
        self.campoDigitos.setFont(QFont("Arial",9))
        self.campoDigitos.setStyleSheet("background-color:#EBE6D2")

        botonGenerar = QPushButton("Generar",panelEstructura)
        botonGenerar.setGeometry(640,100,120,30)
        botonGenerar.setStyleSheet("QPushButton{background-color:#b0c9bb; border:1px solid black;}"
                                        "QPushButton::hover{background-color :#8fa89a;}"
                                        "QPushButton::pressed{background-color:#6e8679; }")
        botonGenerar.setCursor(QCursor(Qt.PointingHandCursor))
        botonGenerar.clicked.connect(self.GenerarEstructura)
        
        self.labelTitIng = QLabel("Ingresar/Buscar",panelEstructura)
        self.labelTitIng.move(120,160)
        self.labelTitIng.setVisible(False)
        
        self.labelCampResNum = QLabel("Clave Numerica",panelEstructura)
        self.labelCampResNum.move(200,185)
        self.labelCampResNum.setFont(QFont("Arial",9,QFont.Bold))
        self.labelCampResNum.setVisible(False)
        self.campoCampResNum = QTextEdit(self)
        self.campoCampResNum.setFrameStyle(1)
        self.campoCampResNum.move(320,200)
        self.campoCampResNum.resize(80,30)
        self.campoCampResNum.setFont(QFont("Arial",9))
        self.campoCampResNum.setVisible(False)
        self.campoCampResNum.setStyleSheet("background-color:#EBE6D2")

        self.labelNombreA = QLabel("Nombre",panelEstructura)
        self.labelNombreA.move(200,225)
        self.labelNombreA.setFont(QFont("Arial",9,QFont.Bold))
        self.labelNombreA.setVisible(False)
        self.campoNombreA = QTextEdit(self)
        self.campoNombreA.setFrameStyle(1)
        self.campoNombreA.move(320,245)
        self.campoNombreA.resize(80,30)
        self.campoNombreA.setFont(QFont("Arial",9))
        self.campoNombreA.setVisible(False)
        self.campoNombreA.setStyleSheet("background-color:#EBE6D2")

        self.labelEdadA = QLabel("Edad",panelEstructura)
        self.labelEdadA.move(200,275)
        self.labelEdadA.setFont(QFont("Arial",9,QFont.Bold))
        self.labelEdadA.setVisible(False)
        self.campoEdadA = QTextEdit(self)
        self.campoEdadA.setFrameStyle(1)
        self.campoEdadA.move(320,290)
        self.campoEdadA.resize(80,30)
        self.campoEdadA.setFont(QFont("Arial",9))
        self.campoEdadA.setVisible(False)
        self.campoEdadA.setStyleSheet("background-color:#EBE6D2")

        self.botonIngresar = QPushButton("Ingresar",panelEstructura)
        self.botonIngresar.setGeometry(420,200,120,30)
        self.botonIngresar.setStyleSheet("QPushButton{background-color:#b0c9bb; border:1px solid black;}"
                                        "QPushButton::hover{background-color :#8fa89a;}"
                                        "QPushButton::pressed{background-color:#6e8679; }")
        self.botonIngresar.setCursor(QCursor(Qt.PointingHandCursor))
        self.botonIngresar.clicked.connect(self.ingresarDato)
        self.botonIngresar.setVisible(False)
        
        
        self.botonBuscar = QPushButton("Buscar",panelEstructura)
        self.botonBuscar.setGeometry(560,200,120,30)
        self.botonBuscar.setStyleSheet("QPushButton{background-color:#b0c9bb; border:1px solid black;}"
                                        "QPushButton::hover{background-color :#8fa89a;}"
                                        "QPushButton::pressed{background-color:#6e8679; }")
        self.botonBuscar.setCursor(QCursor(Qt.PointingHandCursor))
        self.botonBuscar.clicked.connect(self.buscarDato)
        self.botonBuscar.setVisible(False)

        #Consola de salida

        self.registroProcess = QTextEdit(self)
        self.registroProcess.setFrameStyle(1)
        self.registroProcess.setGeometry(10, 350,860, 320)
        self.registroProcess.setReadOnly(True)
        self.registroProcess.setFont(QFont("Arial", 12))
        self.registroProcess.setStyleSheet("QTextEdit{border:1px solid black; background-color:#D0C0A7}")

        
    def GenerarEstructura(self):
        try:
            if self.estructura != None:
                matriz = self.estructura.matriz
            else:
                matriz = []
            if(self.opcionTipoBusq.currentText() == "Secuencial"):
                self.estructura = Secuencial(matriz,int(self.campoRango.toPlainText()),int(self.campoDigitos.toPlainText()))
            elif(self.opcionTipoBusq.currentText() == "Binaria"):
                self.estructura = Binario(matriz,int(self.campoRango.toPlainText()),int(self.campoDigitos.toPlainText()))
            self.tabla.setRowCount(0)
            for x in range(int(self.campoRango.toPlainText())):
                self.tabla.insertRow(x)
            self.labelTitIng.setVisible(True)
            self.labelCampResNum.setVisible(True)
            self.campoCampResNum.setVisible(True)
            self.labelNombreA.setVisible(True)
            self.campoNombreA.setVisible(True)
            self.labelEdadA.setVisible(True)
            self.campoEdadA.setVisible(True)
            self.botonIngresar.setVisible(True)
            self.botonBuscar.setVisible(True)
            self.imprimirTexto("Se ha creado la estructura exitosamente")
            self.refrescarTabla()
        except Exception as e:
            error = QMessageBox()
            error.setText("Los datos no son validos, deben ser Numericos")
            error.setIcon(QMessageBox.Icon.Critical)
            print(e)
            error.exec()

    def deshabilitar(self):
        self.tabla.setRowCount(0)
        self.GenerarEstructura()
        self.refrescarTabla()

    def imprimirTexto(self,texto:str):
        self.registroProcess.setText(self.registroProcess.toPlainText()+"\n >"+texto)

    def ingresarDato(self):
        try:
            res = self.estructura.ingresarDato(int(self.campoCampResNum.toPlainText()))
            self.imprimirTexto(res)
            self.refrescarTabla()
            # nombre = self.estructura.ingresarDato(int(self.campoNombreA.toPlainText()))
            # edad = self.estructura.ingresarDato(int(self.campoEdadA.toPlainText()))
            nombre="juan"
            edad=12
            self.campos.insertar(int(self.campoCampResNum.toPlainText()),nombre,edad)
        except Exception as e:
            error = QMessageBox()
            error.setText("La clave debe ser Numerica")
            error.setIcon(QMessageBox.Icon.Critical)
            print(e)
            error.exec()
    

    def buscarDato(self):
        try:
            res = self.estructura.busqueda(int(self.campoCampResNum.toPlainText()))
            self.imprimirTexto(res)
            self.datoBuscado = int(self.campoCampResNum.toPlainText())
            self.imprimirTexto(self.campos.obtener(self.datoBuscado))
            self.refrescarTabla()
        except Exception as e:
            error = QMessageBox()
            error.setText("la clave debe ser Numerico")
            error.setIcon(QMessageBox.Icon.Critical)
            print(e)
            error.exec()
    
    def refrescarTabla(self):
        for i in range(len(self.estructura.matriz)):
            itemTabla = QTableWidgetItem(("0"*(self.estructura.digitos - len(str(self.estructura.matriz[i]))))+str(self.estructura.matriz[i]))
            if (self.estructura.matriz[i] == self.datoBuscado):
                print("cambiando color")
                itemTabla.setBackground(QColorConstants.Green)
            self.tabla.setItem(i,0,itemTabla)
        self.datoBuscado = None