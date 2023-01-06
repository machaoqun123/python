class Test(object):
	
	def __init__(self):
		self.__num=100##private

	def getNum(self):##getter
		return self.__num

	def setNum(this,num):##setter,第一个参数代表对象，不是关键字，但习惯用self
		if num<100:
			this.__num=num

	num = property(getNum,setNum)
	#num = property(getNum)

t = Test()
t.num = 20
print(t.num)
