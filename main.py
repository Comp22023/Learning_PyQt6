from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QMainWindow
import sys # Только для доступа к аргументам командной строки
from PyQt6.QtCore import QSize, Qt

app = QApplication(sys.argv)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Мое приложение')
        button = QPushButton('Кнопка')

        self.setFixedSize(QSize(400, 300))

        # Устанавливаем центральный виджет Window.
        button.setCheckable(True)
        button.clicked.connect(self.butfunc)
        self.setCentralWidget(button)

    def butfunc(self):
        button = QPushButton('Опа! Вы попали в ловушку джокера...')
        self.setCentralWidget(button)

#window = QPushButton("Push Me") #Кнопка
window =MainWindow()
window.show()  # Важно: окно по умолчанию скрыто.

# Запускаем цикл событий.
app.exec()