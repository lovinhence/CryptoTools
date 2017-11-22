import json
import pyautogui
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
    # t = threading.Thread(target=pyautogui.alert, args=(alert_str,), kwargs={"timeout": 5})
    # t.start()
    pyautogui.alert(alert_str, timeout=5)


def voiceAlert(alert_str):
    pass


if __name__ == '__main__':
    popupAlert("alert")