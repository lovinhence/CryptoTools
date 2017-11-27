import pyttsx3
import win32api


WM_APPCOMMAND = 0x319

APPCOMMAND_VOLUME_MAX = 0x0a
APPCOMMAND_VOLUME_MIN = 0x09

engine = pyttsx3.init()


def say(text):
    engine.say(text)
    engine.runAndWait()

if __name__ == '__main__':
    win32api.SendMessage(-1, WM_APPCOMMAND, 0x30292, APPCOMMAND_VOLUME_MAX * 0x10000)
    say("test test test")



# 音量最大


# 音量最小
# win32api.SendMessage(-1, WM_APPCOMMAND, 0x30292, APPCOMMAND_VOLUME_MIN * 0x10000)
