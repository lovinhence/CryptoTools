import json
import win32api, win32con


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
    win32api.MessageBox(0, alert_str, "title", win32con.MB_OK)


def voiceAlert(alert_str):
    pass


if __name__ == '__main__':
    popupAlert("alert")