from Musica import *

app = QApplication(sys.argv)
ventana = SeleccionArchivoVentana()
ventana.show()
sys.exit(app.exec_())