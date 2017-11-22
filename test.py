import json
import threading
import time


class A():
    def x(self):
        print("ok")


if __name__ == '__main__':
    # try:
    # f = open(".\\config\\exchange.json")
    # jsonObj = json.load(f)
    # except Exception as e:
    # print(str(e))
    # finally:
    # f.close()
    # print(jsonObj['gateio']['className'])

    # s = "abc"
    # s = s.c
    # # s = s.replace("1", "4")
    # print(s)

    # s = "A"
    # obj = eval(s)
    # obj().x()

    def a():
        # while True:
        print("ok")
        print(threading.current_thread().getName())
        time.sleep(1)


    for i in range(10):
        t = threading.Thread(target=a)
        t.start()
