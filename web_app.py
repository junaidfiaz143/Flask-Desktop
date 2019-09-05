import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QUrl
from PyQt5.QtWebEngineWidgets import QWebEngineView

class MyApp(QWidget):

	def __init__(self):
		super().__init__()

		self.initUI()

	def initUI(self):

		self.web = QWebEngineView()
		self.web.setWindowTitle("Artificial Intelligence")
		self.web.setWindowIcon(QIcon("resources/icons/xray.ico"))
		self.web.load(QUrl.fromLocalFile("/resources/configs/html/home.html"))
		self.web.showMaximized()
		# self.web.setFixedSize(1366, 768)
		self.web.show()

if __name__ == '__main__':
	
	app = QApplication(sys.argv)
	my_app = MyApp()
	sys.exit(app.exec_())