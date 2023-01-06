class User(object):
	__instance=None

	def __init__(self,name):
		self.name=name
	
	@classmethod
	def get_instance(cls,name):
		if not cls.__instance:##如果__instance为None
			cls.__instance=User(name)##给__instance赋值实例
		return cls.__instance##第二次再调用时，__instance有值，则不执行if中的代码，直接返回该值，因此无论创建多少对象都是该值（伪单例模式)。

#u1 = User("zs")
#u2 = User("ls")
u1 = User.get_instance("zs")##先执行get_instance方法创建实例然后才执行init方法
u2 = User.get_instance("ls")
print(u1==u2)##判断表达式，如果返回True，这两个对象是一个对象，并且内存地址相同
print("u1对象的内存地址:%s,u2对象的内存地址:%s"%(id(u1),id(u2)))
u3 = User("ww")
print(u1==u3)
print(u1.name)
print(u1.name==u2.name)
