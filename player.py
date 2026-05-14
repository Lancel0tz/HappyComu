import sys
from PyQt5.QtCore import QUrl, QTimer
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMainWindow, QApplication, QLabel, QPushButton
from PyQt5.QtMultimedia import QMediaContent, QMediaPlayer
from PyQt5.QtMultimediaWidgets import QVideoWidget

from multiprocessing import Process, Queue

from record import start_recording, stop_recording

class MainWindow(QMainWindow):
    def __init__(self, queue, parent=None):
        super(MainWindow, self).__init__(parent)
        self.queue = queue
        self.initUI()
        self.startTimer()
        self.resize(600, 600)
        self.is_recording = False

    def initUI(self):
        self.setWindowTitle("Chat Windows")
        self.setGeometry(200, 200, 400, 300)

        self.video_widget = QVideoWidget(self)
        self.video_widget.resize(600, 550)

        self.video_player = QMediaPlayer()
        self.video_player.setVolume(40)
        self.video_player.setVideoOutput(self.video_widget)

        # 添加一个按钮来开始录音
        self.record_button = QPushButton('点击对话', self)
        self.record_button.resize(600, 50)
        self.record_button.move(0, 550)  # 按钮的位置
        self.record_button.clicked.connect(self.startRecording)

        self.show()

    def startTimer(self):
        # 设置一个定时器来定期检查队列
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.updateFromQueue)
        self.timer.start(1000)  # 每秒更新一次

    def updateFromQueue(self):
        if not self.queue.empty():
            file = self.queue.get()
            self.video_player.setMedia(QMediaContent(QUrl.fromLocalFile(file)))
            self.video_player.play()

    def closeEvent(self, event):
        # 你可以在这里设置一个全局变量或者发送一个信号来通知后台进程终止
        global exit_code
        exit_code = 0
        event.accept()  # 接受关闭事件

    def startRecording(self):
        if not self.is_recording:
            start_recording()
            self.record_button.setText("停止对话")
            self.is_recording = True
        else:
            stop_recording()  # 停止录音的函数
            self.record_button.setText("点击对话")
            self.is_recording = False



if __name__ == '__main__':
    app = QApplication(sys.argv)
    queue = Queue()
    queue.put(r".\results\2023_11_21_14.15.04.mp4")
    window = MainWindow(queue)
    sys.exit(app.exec_())


