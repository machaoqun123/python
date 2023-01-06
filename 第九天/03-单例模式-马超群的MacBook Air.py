class User(object):
	__instance=None

	def __init__(self,name):
		self.name=name
	
	def __new__(cls,name):##保证new方法只调用一次
		if not cls.__instance:
			cls.__instance=object.__new__(cls)
		return cls.__instance
			

u1 = User("zs")
u2 = User("ls")
u3 = object.__new__(User)##不会帮助调init方法
print(u1==u3)
##执行13行，则先第一次自动调用new方法，然后第一次自动调用init方法，进而self.name被"zs"赋值；再执行14行，此时第二次自动调用new方法，然而由于__instance=User（”zs“）,则直接返回__instance；
##接下来第二次自动调用init方法时，self依然指的是u1，因此self.name=name意味着将实参（ls）赋值给u1的属性name。
#print(u1==u2)##判断表达式，如果返回True，这两个对象是一个对象，并且内存地址相同
#print("u1对象的内存地址:%s,u2对象的内存地址:%s"%(id(u1),id(u2)))
print(u1.name)
print(u2.name)
