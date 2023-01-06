class User(object):
	
	def __init__(self,username,password):##User子类重写了object父类中的init方法
		self.username=username
		self.password=password
		print("对象已经构建好了，由解释器自动回调init方法，对象初始化")

	
	#new方法是当时对象构建的时候由解释器自动回调的方法。该方法必须要返回当前类的对象。
	def __new__(cls,username,password):##只有带有默认参数
		print("User类的对象开始构建")
		return	object.__new__(cls)##如果没有此行代码，则不能构建当前类对象，进而不能初始化	

	def __str__(self):
		return "用户名%s,密码%s"%(self.username,self.password)

u = User("zs","123")
print(u)
		
