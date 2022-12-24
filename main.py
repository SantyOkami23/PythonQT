import sys
from PyQt5 import uic, QtWidgets,QtCore,QtGui
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtWidgets import *

class AdmVivero(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('GuiApp.ui', self)

        self.pushButtonAgregarProp.clicked.connect(self.registrarProp)
        self.pushButtonAgregarFinca.clicked.connect(self.registrarFinca)

    def registrarProp(self):
        popUp = QMessageBox()

        if '' in [self.lineEditIdentidad.text(), self.lineEditNombre.text(), self.lineEditApellido.text(),
                  self.lineEditTel.text(), self.lineEditCorreo.text()]:
            popUp.setIcon(QMessageBox.Critical)
            popUp.setWindowTitle('ERROR')
            popUp.setText('Error al insertar Productor')
            popUp.exec_()
        else:
            popUp.setIcon(QMessageBox.Information)
            popUp.setWindowTitle('REGISTRO EXITOSO')
            popUp.setText('Productor agregado')
            popUp.exec_()

    def registrarFinca(self):
        popUp = QMessageBox()
        comboBox = self.comboBoxCultivo.currentText()
        print(comboBox)

        if '' in [self.lineEditMunicipio.text(), self.lineEditRegCastral.text()] and self.comboBoxCultivo.currentText()\
                == 'Seleccione el cultivo...':
            popUp.setIcon(QMessageBox.Critical)
            popUp.setWindowTitle('ERROR')
            popUp.setText('Error al insertar Finca')
            popUp.exec_()
        else:
            self.lineEditMunicipio.clear()
            self.lineEditRegCastral.clear()
            popUp.setIcon(QMessageBox.Information)
            popUp.setWindowTitle('REGISTRO EXITOSO')
            popUp.setText('Finca agregada')
            popUp.exec_()




if __name__ == '__main__':
    app = QApplication(sys.argv)
    GUI = AdmVivero()
    GUI.show()
    sys.exit(app.exec_())



