import os
import sys
import pyttsx3


class TTS:

    # 초기화
    def __init__(self):
        self.engine = pyttsx3.init()

    def tts(self, txt):
        self.engine.say(txt)  # 입력한 텍스트 내용을 음성으로 나타냄
        self.engine.runAndWait()  # 엔진을 실행하고 대기
