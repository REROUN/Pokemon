import os
import sys
import speech_recognition as sr  # 음성 분석석


class STT:

    # 초기화
    def __init__(self):
        self.recognizer = sr.Recognizer()

    # 마이크에서 입력받기
    def stt(self):

        with sr.Microphone() as source:
            audio = self.recognizer.listen(source, phrase_time_limit=10)

        try:
            txt = self.recognizer.recognize_google(audio, language="ko-KR")
        except sr.UnknownValueError:
            return "Google Web Speech API가 당신의 말을 이해하지 못했습니다."
        except sr.RequestError as e:
            return f"Google Web Speech API 서비스에 문제가 발생했습니다; {e}"
        else:
            return txt
