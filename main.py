import sys
import random

from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QApplication, QMainWindow
from UI import Ui_MainWindow


# Наследуемся от виджета из PyQt5.QtWidgets и от класса с интерфейсом
class MyWidget(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        # Вызываем метод для загрузки интерфейса из класса Ui_MainWindow,
        # остальное без изменений
        self.setupUi(self)

        self.r1 = 0

        self.pushButton.clicked.connect(self.run)

    def run(self):
        # Определяем радиус
        self.r1 = random.randint(10, 150)
        self.repaint()

    def paintEvent(self, event):
        if (self.r1 > 0):
            qp = QPainter()
            qp.begin(self)

            x = random.randint(self.r1, self.geometry().width() - self.r1)
            y = random.randint(self.r1, self.geometry().height() - self.r1)

            qp.setBrush(QColor(255, 255, 0))
            qp.drawEllipse(x, y, self.r1, self.r1)

            qp.end()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())
