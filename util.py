import json
import win32api, win32con
import pyttsx3
import threading


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
    # win32api.Mess
    win32api.MessageBox(0, alert_str, "title", win32con.MB_OK)


def voiceAlert(alert_str):
    engine = pyttsx3.init()
    engine.say(alert_str)
    engine.runAndWait()


def alert(alert_str):
    t1 = threading.Thread(target=popupAlert, args=(alert_str,))
    t1.start()
    t2 = threading.Thread(target=voiceAlert, args=(alert_str,))
    t2.start()


if __name__ == '__main__':
    popupAlert("alert")
