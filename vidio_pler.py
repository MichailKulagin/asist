from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QLabel
from PyQt5.QtMultimediaWidgets import QVideoWidget
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from PyQt5.QtCore import QUrl

class VideoPlayer(QWidget):
    def __init__(self):
        super().__init__()

        # create the video player
        self.mediaPlayer = QMediaPlayer(None, QMediaPlayer.VideoSurface)

        # create the video widget
        videoWidget = QVideoWidget()

        # set the video output to the widget
        self.mediaPlayer.setVideoOutput(videoWidget)

        # create the play button, connect it to the media player
        playButton = QPushButton("Включить")
        playButton.clicked.connect(self.play)

        # create a layout
        layout = QVBoxLayout()
        layout.addWidget(videoWidget)
        layout.addWidget(playButton)

        # set the layout on the window
        self.setLayout(layout)

        # set the properties of the window
        self.setWindowTitle("Видео плеер")
        self.setGeometry(100, 100, 800, 600)

    def play(self):
        try:
            videoFile = "i.mp4"
            self.mediaPlayer.setMedia(QMediaContent(QUrl.fromLocalFile(videoFile)))
            self.mediaPlayer.play()
        except:
            print('Ошипка')

if __name__ == "__main__":
    app = QApplication([])
    window = VideoPlayer()
    window.show()
    app.exec_()
