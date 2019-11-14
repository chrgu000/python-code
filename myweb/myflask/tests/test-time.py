######### 测试日期 Begin ########
# import time
# from datetime import datetime

# t1 = time.time()
# t2 = time.strftime("%Y%m%d %H:%M:%S", time.localtime(t1))
# print(t1, type(t1), int(t1), t2)

######### 测试日期 End ########


######### 测试json Begin ########
import json
d = {"name": "Bob", "age" : 12}
print(type(d), d)
d = json.dumps(d)
print(type(d), d)
d = json.loads(d)
print(type(d), d)