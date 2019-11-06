import time
from datetime import datetime

t1 = time.time()
t2 = time.strftime("%Y%m%d %H:%M:%S", time.localtime(t1))
print(t1, type(t1), int(t1), t2)