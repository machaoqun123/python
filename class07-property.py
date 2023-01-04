class User(object):
	name="zs"##公共的类属性
	__password="123456"##私有的类属性

	def __init__(self,sex,username,age):
		self.sex=sex
		self.username=username ##对象属性
		self.__age=age
	def __str__(self):
		return self.__age

#每个对象都可以有不同的属性
u = User("男","goldbin","18")
print(u)
print(u.name)

u2 = User("","sdfs","")
print(u2.name)
