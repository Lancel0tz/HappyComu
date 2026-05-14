import sounddevice as sd
from scipy.io.wavfile import write
import numpy as np
import time

is_recording = False
stream = None
recording = []

def record_callback(indata, frames, time, status):
    recording.extend(indata.copy())

def start_recording():
    global is_recording, recording, stream
    recording = []
    is_recording = True
    print("正在录音......")
    stream = sd.InputStream(callback=record_callback, samplerate=48000, channels=2)
    stream.start()

def stop_recording():
    global is_recording, stream
    is_recording = False
    if stream:
        stream.stop()
        stream.close()
        print("录音结束......")
    write(r'.\audioflow\output.mp3', 48000, np.array(recording))  # 保存为MP3文件

if __name__ == '__main__':
    start_recording()
    time.sleep(5)
    stop_recording()
