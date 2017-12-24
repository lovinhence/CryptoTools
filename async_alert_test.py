import time

# alert_list = [("test1", 5), ("test2", 5)]
# while True:
#     for i in range(len(alert_list)):
#         alert_str, ttl = alert_list[i]
#         ttl -= 1
#         if ttl > 0:
#             alert_list[i] = (alert_str, ttl)
#         else:
#
#     print(alert_list)
#     time.sleep(1)

stack = [1,2,3,4,5]
if len(stack) >= 5:
    stack.pop()
    stack.append(6)
print(stack)

