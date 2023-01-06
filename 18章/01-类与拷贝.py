class Person(object):
	num=100
	def __init__(self,name,age):
		self.name=name
		self.age=age
	
	def showInfo(self):
		print(self.name)
		print(self.age)

	@classmethod
	def printNum(cls):
		print(cls.num)
		
	@staticmethod
	def add(a,b):
		return a+b
		

p1 = Person("zs","18")
p1.showInfo()
p1.printNum()
Person.printNum()
print(p1.add(10,20))
print(Person.add(10,20))
