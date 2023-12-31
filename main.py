from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QMainWindow
import sys  # Только для доступа к аргументам командной строки
from PyQt6.QtCore import QSize, Qt

app = QApplication(sys.argv)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Мое приложение')
        self.resize(400, 300)  # Размеры окна

        button = QPushButton('Кнопка')
        button.setCheckable(True)
        button.clicked.connect(self.butfunc)
        self.setCentralWidget(button)  # Устанавливаем центральный виджет Window.

    def butfunc(self):
        self.setWindowTitle("Вы были пойманы... Пока-капа...")
        button = QPushButton('Опа! Вы попали в ловушку джокера...')
        button.setGeometry(10, 10, 10, 10)
        button.adjustSize()
        self.setCentralWidget(button)


# window = QPushButton("Push Me") #Кнопка
window = MainWindow()
window.show()  # Важно: окно по умолчанию скрыто.

# Запускаем цикл событий.
app.exec()
