import json
import win32api, win32con
import pyttsx3
import time
import logging
from logging.handlers import RotatingFileHandler

voiceTaskList = []
logger = logging.getLogger()

# 定义一个RotatingFileHandler，最多备份5个日志文件，每个日志文件最大10M
rtHandler = RotatingFileHandler('.\\log\\log.txt', maxBytes=10 * 1024 * 1024, backupCount=5)
rtHandler.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s:%(message)s')
rtHandler.setFormatter(formatter)
logger.addHandler(rtHandler)

def getGlobalConfig():
    try:
        f = open(".\\config\\exchange.json")
        jsonObj = json.load(f)
        return jsonObj
    except Exception as e:
        print(str(e))
    finally:
        f.close()


def getExchangeConfigJson():
    try:
        f = open(".\\config\\exchange.json")
        jsonObj = json.load(f)
        return jsonObj
    except Exception as e:
        print(str(e))
    finally:
        f.close()


def popupAlert(alert_str):
    win32api.MessageBox(0, alert_str, "title", win32con.MB_OK, 1)
    # win32api.MessageBox(0, al
    # ert_str, "title", 0,200)
    # win32api.MessageBoxEx(0, alert_str, "title",1,1)


def voiceAlert(alert_str):
    engine = pyttsx3.init()
    engine.say(alert_str)
    engine.runAndWait()


def alert(alert_str):
    if len(voiceTaskList) >= 3:
        voiceTaskList.pop(0)
    voiceTaskList.append(alert_str)


def realAlert(alert_str):
    # cut src and ratio str
    alert_str = alert_str.split(" ")[-1]
    voiceAlert(alert_str)
    # popupAlert(alert_str)


# 告警逻辑改为异步队列形式。
# 消息需要听时效性最高的，所以用长度有限的stack做数据结构
class AlertEngine():
    def mainLoop(self):
        while True:
            if len(voiceTaskList) > 0:
                alert_str = voiceTaskList.pop()
                realAlert(alert_str)
                logger.error(alert_str)
            time.sleep(0.5)

globalConfig = getGlobalConfig()
exchangeConfigJson = getExchangeConfigJson()
alertEngine = AlertEngine()

if __name__ == '__main__':
    voiceAlert("cdt cdt,gateio buy,binance sell:0.961615")
