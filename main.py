import glob
from base64 import b64encode
import os, sys, time
from multiprocessing import Process, Queue

from player import MainWindow
from inference import infer, parse_arguments
from respond import respond
import setup

from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton
from PyQt5.QtCore import QUrl, QTimer
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from PyQt5.QtMultimediaWidgets import QVideoWidget
from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow

import torch
from argparse import ArgumentParser

conversation_history = [f"从现在开始，你需要扮演下面的角色来回答我的任何后续问题({setup.CHAR1}，你需要扮演的更加自然，就像和我再聊天闲谈一样，下面是我们的聊天记录，你需要对最下面还未回答的问题作出回应(你只有150tokens的输出，请在150tokens内保证回答语句的完整):"]

def main_loop(queue):
    audio = './examples/driven_audio/response.mp3' ###
    global exit_code
    exit_code = 1
    while True:
        # Break the loop if the window was closed
        if exit_code != 1:
            sys.exit()
        respond()
        if os.path.exists(audio) and os.path.getsize(audio) > 0:
            print("正在思考......")
            args = parse_arguments()
            if torch.cuda.is_available() and not args.cpu:
                args.device = "cuda"
            else:
                args.device = "cpu"
            infer(args) #推理生成

            # 获取 MP4 文件的路径
            results = sorted(os.listdir('./results/'))
            mp4_name = glob.glob('./results/*.mp4')[-1]

            # 将 mp4 文件名添加到队列
            queue.put(mp4_name)
            os.remove(audio)

        else:
            # Wait for a short period before checking again
            time.sleep(0.5)

if __name__ == '__main__':
    app = QApplication(sys.argv)

    queue = Queue()
    worker = Process(target=main_loop, args=(queue,))
    worker.start()

    queue.put(r".\examples\ref_video\Untitled video (2).mp4")
    window = MainWindow(queue)
    window.show()
    app.exec_()

    # 确保在退出时终止后台进程
    worker.terminate()
    worker.join()

