#-*- coding: utf-8 -*-

'''
装饰器

'''

import time

def timing(func):
	def funcNew():
		startTime = time.time()
		func()
		endTime = (time.time()-startTime)*1000
		print('耗时（毫秒）： %f' % (endTime))
	return funcNew


@timing   #等同下边主体中的 myfunc = timing(myfunc)
def myfunc():
	print('stat =========>>>>>>>>>')
	time.sleep(2)
	print('<<<<<<<<<<<<<==========end')

print("myfunc is  ", myfunc.__name__)
# myfunc = timing(myfunc)
print('#'*40)
print("myfunc is  ", myfunc.__name__)
myfunc()

print("myfunc is  ", myfunc.__name__)