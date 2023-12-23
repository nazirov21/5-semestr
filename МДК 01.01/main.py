import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel, QMainWindow, QAction, QTextEdit, \
    QStackedWidget, QGridLayout
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from PyQt5.QtMultimediaWidgets import QVideoWidget
from PyQt5.QtCore import QUrl
from PyQt5.QtGui import QPixmap


class MainApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Приложение')

        nav_menu = self.menuBar()
        page1_action = QAction('Главная страница', self)
        page1_action.triggered.connect(self.show_page1)
        page2_action = QAction('Видео', self)
        page2_action.triggered.connect(self.show_page2)
        nav_menu.addAction(page1_action)
        nav_menu.addAction(page2_action)

        self.stacked_widget = QStackedWidget()
        self.setCentralWidget(self.stacked_widget)

        self.page1 = QWidget()
        label1 = QLabel('план производства вместе с Акбаром вместе все просчитывали где что будет стоять то есть Акбар все расставлял а я все придумывал  Проект настольного приложения, я отвечал за весь код  3д модельки идея была моя но воплотил ее АкбFH  Прототип мобильного приложения в figme делал я ')
        self.page1.layout = QVBoxLayout()
        self.page1.layout.addWidget(label1)

        logo_label = QLabel()
        pixmap = QPixmap('aEzcYUGedmo.png')
        logo_label.setPixmap(pixmap)
        self.page1.layout.addWidget(logo_label)

        self.page1.setLayout(self.page1.layout)
        self.stacked_widget.addWidget(self.page1)

        self.page2 = QWidget()
        label2 = QLabel('МДК 01 01 – сделан сайт, есть 3 сертификата и сдана прибыль МДК 01.04 установка виртуал бокса установка ред ос установка авалони Численные  методы – сдано все что касается матриц то есть excel код в реплите и отчет  Уравнения все выполнены и так же сданы отче по слау тоже сдан  Что касается уп оформление документов делал я Код будущего закрыт первый модуль успел так сказать')
        video_widget = QVideoWidget()
        self.video_player = QMediaPlayer(None, QMediaPlayer.VideoSurface)
        self.video_player.setVideoOutput(video_widget)
        self.video_player.setMedia(QMediaContent(QUrl.fromLocalFile('VID_20231223_121454_224.mp4')))
        self.play_button = QPushButton('Жмякни для запуска')
        self.play_button.clicked.connect(self.play_video)
        self.back_button = QPushButton('Back')
        self.back_button.clicked.connect(self.show_page1)
        self.page2.layout = QVBoxLayout()
        self.page2.layout.addWidget(label2)
        self.page2.layout.addWidget(video_widget)
        self.page2.layout.addWidget(self.play_button)
        self.page2.layout.addWidget(self.back_button)
        self.page2.setLayout(self.page2.layout)
        self.stacked_widget.addWidget(self.page2)

    def show_page1(self):
        self.stacked_widget.setCurrentIndex(0)
        self.back_button.hide()

    def show_page2(self):
        self.stacked_widget.setCurrentIndex(1)
        self.back_button.show()

    def play_video(self):
        self.video_player.play()
        self.back_button.hide()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_app = MainApp()
    main_app.show()
    sys.exit(app.exec())