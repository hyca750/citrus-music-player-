# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'reproductor.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent, QMediaMetaData
from PyQt5.QtCore import QUrl

# biblografia https://doc.qt.io/qt-5/qmediaplayer.html 
class Ui_reproductor(object): 

    def setupUi(self, reproductor):
        # Configuración player
        self.player = QMediaPlayer() # ejecutamos la funcion que inicializa el reproductor
        self.player.setVolume(100) # definimos el voluem del reproductor
        self.player.positionChanged.connect(self.ubicacion) # usamos el conect para conectar una posion de la barra con una fucnion
        self.player.durationChanged.connect(self.tiempo) # lo mismo pero con la barra que muestra el progreso
        self.player.stateChanged.connect(self.reproduccion) # conectamos con la funcion para ejecutar la cancion con los botones
        self.player.mediaStatusChanged.connect(lambda: self.infocancion()) # usamoe el status changed para definir los metadatos # funcion al dar pausa ala cancion un pequeño bug 
        reproductor.setObjectName("reproductor")
        reproductor.resize(597, 542)
        reproductor.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("limon.png"),
                       QtGui.QIcon.Normal, QtGui.QIcon.Off)
        reproductor.setWindowIcon(icon)
        reproductor.setToolTip("")
        reproductor.setStyleSheet(
            "background-color: qlineargradient(spread:repeat, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 255, 255, 255), stop:0.994318 rgba(122, 219, 160, 255));")
        reproductor.setIconSize(QtCore.QSize(30, 30))
        reproductor.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        reproductor.setTabShape(QtWidgets.QTabWidget.Triangular)
        self.centralwidget = QtWidgets.QWidget(reproductor)
        self.centralwidget.setObjectName("centralwidget")
        self.sicancion = QtWidgets.QPushButton(self.centralwidget)
        self.sicancion.setGeometry(QtCore.QRect(430, 400, 90, 80))
        self.sicancion.setStyleSheet("border-radius: 40px;\n"
                                     "border-style:solid;\n"
                                     "\n"
                                     "")
        self.sicancion.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("adelantar cancion.png"),
                        QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.sicancion.setIcon(icon1)
        self.sicancion.setIconSize(QtCore.QSize(50, 50))
        self.sicancion.setObjectName("sicancion")
        self.sicancion.clicked.connect(self.cancionqsigue)
        self.antcancion = QtWidgets.QPushButton(self.centralwidget)
        self.antcancion.setGeometry(QtCore.QRect(190, 400, 90, 81))
        self.antcancion.setStyleSheet("border-radius: 40px;\n"
                                      "border-style:solid;\n"
                                      "")
        self.antcancion.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("devolver cancion.png"),
                        QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.antcancion.setIcon(icon2)
        self.antcancion.setIconSize(QtCore.QSize(50, 50))
        self.antcancion.setObjectName("antcancion")
        self.antcancion.clicked.connect(self.cancionpasada)
        self.botonplay = QtWidgets.QPushButton(self.centralwidget)
        self.botonplay.setGeometry(QtCore.QRect(310, 400, 90, 80))
        self.botonplay.setStyleSheet("border-radius: 40px;\n"
                                     "border-color: rgb(0, 0, 0);\n"
                                     "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(66, 255, 184, 255), stop:1 rgba(255, 255, 255, 255));\n"
                                     "")
        self.botonplay.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("boton-de-play.png"),
                        QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.botonplay.setIcon(icon3)
        self.botonplay.setIconSize(QtCore.QSize(50, 50))
        self.botonplay.setObjectName("botonplay")
        self.botonplay.clicked.connect(self.reproducir)
        self.barracancion = QtWidgets.QSlider(self.centralwidget)
        self.barracancion.setGeometry(QtCore.QRect(200, 330, 301, 21))
        self.barracancion.setMinimumSize(QtCore.QSize(18, 18))
        self.barracancion.setStyleSheet("QhorizontalSlider{\n"
                                        "border-style:solid;\n"
                                        "background-color: rgb(41, 170, 144);\n"
                                        "}\n"
                                        "QSlider::handle:horizontal{\n"
                                        "background-color: rgb(33, 55, 255);\n"
                                        "border-radius:19px;\n"
                                        "border-color:rgb(33, 55, 255);\n"
                                        "}")
        self.barracancion.setOrientation(QtCore.Qt.Horizontal)
        self.barracancion.setObjectName("barracancion")
        self.barracancion.sliderMoved.connect(
            lambda x: self.player.setPosition(x))
        self.volumen = QtWidgets.QSlider(self.centralwidget)
        self.volumen.setGeometry(QtCore.QRect(540, 140, 21, 131))
        self.volumen.setStyleSheet("QVerticalSlider{\n"
                                   "color: qlineargradient(spread:repeat, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 255, 255, 255), stop:0.994318 rgba(122, 219, 160, 255));\n"
                                   "border-style:solid;\n"
                                   "\n"
                                   "}")
        self.volumen.setOrientation(QtCore.Qt.Vertical)
        self.volumen.setObjectName("volumen")
        self.volumen.valueChanged.connect(self.movervolumen)
        self.artista = QtWidgets.QLabel(self.centralwidget)
        self.artista.setGeometry(QtCore.QRect(270, 40, 141, 21))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic Medium")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(7)
        self.artista.setFont(font)
        self.artista.setStyleSheet("font: 57 11pt \"Yu Gothic Medium\";")
        self.artista.setText("")
        self.artista.setAlignment(QtCore.Qt.AlignCenter)
        self.artista.setObjectName("artista")
        self.titulocancion = QtWidgets.QLabel(self.centralwidget)
        self.titulocancion.setGeometry(QtCore.QRect(260, 0, 161, 21))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.titulocancion.setFont(font)
        self.titulocancion.setStyleSheet("font: 75 12pt \"Yu Gothic UI\";")
        self.titulocancion.setText("")
        self.titulocancion.setAlignment(QtCore.Qt.AlignCenter)
        self.titulocancion.setObjectName("titulocancion")
        self.archivo = QtWidgets.QPushButton(self.centralwidget)
        self.archivo.setGeometry(QtCore.QRect(40, 390, 91, 71))
        self.archivo.setStyleSheet("\n"
                                   "border-radius: 30 px;\n"
                                   "border-style:solid;\n"
                                   "")
        self.archivo.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("carpeta.png"),
                        QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.archivo.setIcon(icon4)
        self.archivo.setIconSize(QtCore.QSize(38, 38))
        self.archivo.setObjectName("archivo")
        self.archivo.clicked.connect(self.abrir)
        self.barracancion_2 = QtWidgets.QProgressBar(self.centralwidget)
        self.barracancion_2.setGeometry(QtCore.QRect(200, 290, 301, 16))
        self.barracancion_2.setStyleSheet("QProgressBar\n"
                                          "{\n"
                                          "border: solid grey;\n"
                                          "border-radius: 60px;\n"
                                          "background-color: rgb(41, 170, 144);\n"
                                          "\n"
                                          "}\n"
                                          "QProgressBar::chunk \n"
                                          "{\n"
                                          "background-color: #05B8CC;\n"
                                          "border-radius :30px;\n"
                                          "}      ")
        self.barracancion_2.setProperty("value", 24)
        self.barracancion_2.setTextVisible(False)
        self.barracancion_2.setObjectName("barracancion_2")
        self.inicio = QtWidgets.QLabel(self.centralwidget)
        self.inicio.setGeometry(QtCore.QRect(200, 360, 47, 13))
        self.inicio.setText("")
        self.inicio.setAlignment(QtCore.Qt.AlignCenter)
        self.inicio.setObjectName("inicio")
        self.fin = QtWidgets.QLabel(self.centralwidget)
        self.fin.setGeometry(QtCore.QRect(460, 360, 47, 13))
        self.fin.setText("")
        self.fin.setAlignment(QtCore.Qt.AlignCenter)
        self.fin.setObjectName("fin")
        self.pausa = QtWidgets.QPushButton(self.centralwidget)
        self.pausa.setGeometry(QtCore.QRect(310, 400, 90, 80))
        self.pausa.setStyleSheet("border-radius: 40px;\n"
                                 "border-color: rgb(0, 0, 0);\n"
                                 "\n"
                                 "background-color: rgb(85, 255, 255);")
        self.pausa.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("pausar.png"),
                        QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pausa.setIcon(icon5)
        self.pausa.setIconSize(QtCore.QSize(50, 50))
        self.pausa.setObjectName("pausa")
        self.pausa.clicked.connect(self.pausar)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(100, 0, 71, 61))
        self.label.setStyleSheet("border-radius:30px;")
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("limon.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.boton = QtWidgets.QPushButton(self.centralwidget)
        self.boton.setGeometry(QtCore.QRect(530, 60, 40, 43))
        self.boton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.boton.setStatusTip("")
        self.boton.setStyleSheet("QPushButton{ \n"
                                 "border-radius:30 px;\n"
                                 "}\n"
                                 "\n"
                                 "")
        self.boton.setText("")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("speaker.png"),
                        QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.boton.setIcon(icon6)
        self.boton.setIconSize(QtCore.QSize(50, 50))
        self.boton.setObjectName("boton")
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(20, 80, 151, 271))
        self.listWidget.setStyleSheet("border-radius:30 px;\n"
                                      "border-style:solid;")
        self.listWidget.setObjectName("listWidget")
        self.listWidget.itemClicked.connect(self.cancion)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(200, 80, 291, 191))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("musica.png"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        reproductor.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(reproductor)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 597, 21))
        self.menubar.setObjectName("menubar")
        reproductor.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(reproductor)
        self.statusbar.setObjectName("statusbar")
        reproductor.setStatusBar(self.statusbar)

        self.retranslateUi(reproductor)
        QtCore.QMetaObject.connectSlotsByName(reproductor)
###3333333333333333333333333333333333333333333333333333322222222222222244444444444444444444441111111111111111111113333333333333222222222222111111111#
        # Valores Iniciales
        self.volumen.setValue(100) # establcemos el volumen usando la funcion setvalue
        self.barracancion.setValue(0) # inicializamos valores en la barra de progreso
        self.barracancion_2.setValue(0) # inicializamos valores en la barra de pocision
        self.inicio.setText("00:00") # inicializamos valores en el label 1 de tiempo
        self.fin.setText("00:00")# inicializamos valores en el label 1 de tiempo

    # Funciones

    def abrir(self):# definimos la funcion para abrir archivo
        rutas = QFileDialog.getOpenFileNames(    # usamos la funcion de qfile para abrir archivos 
            self.archivo, "Abrir archivo", "", "Audio files (*.mp3 *.ogg *.wav)") # definimos el filtro
        if rutas:    
            self.listWidget.addItems(rutas[0])
            self.player.setMedia(QMediaContent(
                QUrl.fromLocalFile(rutas[0][0])))
            self.reproducir()

    def reproducir(self): # definimos el la funcion para reproducir la cancion
        self.infocancion() 
        self.player.play()

    def pausar(self): # definimos la funcion para la puasa
        self.player.pause()

    def movervolumen(self): # funcion para mover el volumen
        self.player.setVolume(self.volumen.value())
     
    def infocancion(self): # funcion para mostrar los datos de la cnacion en display
        titulo = 'Sin titulo'
        artista = 'Sin artista'
        if self.player.isMetaDataAvailable():# esta es una funcion de la librearia qmediaplayer
            titulo = self.player.metaData(QMediaMetaData.Title) # llamos la funcion metadata con el parametro
            artista = self.player.metaData(QMediaMetaData.AlbumArtist)
        self.artista.setText(artista) # usamos el set text para mostrar en pantalla
        self.titulocancion.setText(titulo)
   
   
    def tiempo(self, tiempo): # funcion de tiempo
        self.barracancion.setRange(0, tiempo) # definimos el rango y usamos el parametro tiempo
        self.barracancion_2.setRange(0, tiempo)
        minutos, segundos = divmod(tiempo*0.001, 60) # funcion para mostrar los segundos
        self.fin.setText("{:02d}:{:02d}".format(  # definimos los formatos de tiempo
            int(minutos), int(segundos)))

    def ubicacion(self, tiempo): # lo mismo de la anterior pero definimos value
        self.barracancion.setValue(tiempo)
        self.barracancion_2.setValue(tiempo)
        minutos, segundos = divmod(tiempo*0.001, 60)
        self.inicio.setText("{:02d}:{:02d}".format(
            int(minutos), int(segundos)))

    def reproduccion(self):  # funcion para el boton de play para que se esconda
        if self.player.state() == QMediaPlayer.PlayingState: # usamos el la funcion state para definir uno
            self.botonplay.hide() # acciones que va a hacer la funcion
            self.pausa.show()
        else: 
            self.pausa.hide()
            self.botonplay.show()

    def cancionqsigue(self):
        if self.listWidget.currentRow() < self.listWidget.count() - 1: # definimos una especie de contador para las cancion que han sido abiertas
            self.listWidget.setCurrentRow(self.listWidget.currentRow() + 1)
            self.player.setMedia(QMediaContent(QUrl.fromLocalFile( #llamamos ala funcion de de qurl para establecer las canciones
                self.listWidget.currentItem().text())))
            self.reproducir()

    def cancionpasada(self):
        if self.listWidget.currentRow() > 0: # lo mismo que la anterior pero cambiando los valores a ejecutar dento del contador
            self.listWidget.setCurrentRow(self.listWidget.currentRow() - 1)
            self.player.setMedia(QMediaContent(QUrl.fromLocalFile(
                self.listWidget.currentItem().text())))
            self.reproducir()

   

    def cancion(self): # definimos las funcion que ejecute la cancion
        self.player.setMedia(QMediaContent(QUrl.fromLocalFile( # usamos la funcion set media para realizar el proceso del archivo de musica
            self.listWidget.currentItem().text())))
        self.reproducir()

    def retranslateUi(self, reproductor):
        _translate = QtCore.QCoreApplication.translate
        reproductor.setWindowTitle(_translate(
            "reproductor", "Citrus Music 1.0"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    reproductor = QtWidgets.QMainWindow()
    ui = Ui_reproductor()
    ui.setupUi(reproductor)
    reproductor.show()
    sys.exit(app.exec_())
