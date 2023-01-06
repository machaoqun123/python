class Test(object):
	
	def __init__(self):
		self.__num=100##private
	
	@property
	def num(self):##getter
		return self.__num
	
	@num.setter
	def num(this,num):##setter,第一个参数代表对象，不是关键字，但习惯用self
		if num<100:
			this.__num=num


t = Test()
#t.num = 20##需要setter方法则需要这一行代码，这用于赋值；直接获得对象的私有属性则不需要此行代码
print(t.num)
