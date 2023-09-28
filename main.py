from PyQt6.QtWidgets import QApplication, QPushButton, QMainWindow, QGridLayout, QWidget
import sys  # Только для доступа к аргументам командной строки
from PyQt6.QtCore import QSize, Qt

app = QApplication(sys.argv)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        window = QWidget()
        self.setWindowTitle('Мое приложение')
        self.resize(500, 500)  # Размеры окна
        button = QPushButton('Кнопка')
        button.setCheckable(True)
        button.clicked.connect(self.butfunc)
        self.setCentralWidget(button)  # Устанавливаем центральный виджет Window.
        button.setFixedSize(100, 60)
        button.move(100, 100)
        layout = QGridLayout

    def butfunc(self):
        self.setWindowTitle("Вы были пойманы... Пока-капа...")
        self.button = QPushButton('Опа! Вы попали в ловушку джокера...')
        self.button.setGeometry(10, 10, 10, 10)
        self.button.adjustSize()
        self.setCentralWidget(self.button)
        self.button.setFixedSize(100, 60)
        self.button.move(100,100)


# window = QPushButton("Push Me") #Кнопка
window = MainWindow()
window.show()  # Важно: окно по умолчанию скрыто.

# Запускаем цикл событий.
app.exec()
