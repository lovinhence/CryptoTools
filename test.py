import json

class A():
    def x(self):
        print("ok")

if __name__ == '__main__':
    # try:
    # f = open(".\\config\\exchange.json")
    #     jsonObj = json.load(f)
    # except Exception as e:
    #     print(str(e))
    # finally:
    #     f.close()
    # print(jsonObj['gateio']['className'])

    # s = "abc"
    # s = s.c
    # # s = s.replace("1", "4")
    # print(s)

    s = "A"
    obj = eval(s)
    obj().x()