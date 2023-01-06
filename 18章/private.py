class Test(object):
	
	def __init__(self):
		self.__num=100

	def readNum(self):
		print(self.__num)

	def __str__(self):
		print("自动执行str方法")
		return "类中的对象私有属性为:%s"%self.__num


#t = Test()
#print(t.__num)
