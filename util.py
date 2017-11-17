import json

def getExchangeConfigJson():
    try:
        f = open(".\\config\\exchange.json")
        jsonObj = json.load(f)
        return jsonObj
    except Exception as e:
        print(str(e))
    finally:
        f.close()
