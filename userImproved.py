class User:

	def __init__(self,pw):
		if len(pw)>=6:
		#__password 是隐藏属性，必须在类内提供方法获取
			self.__password=pw
		else:
			print("密码%s不符合规定"%pw)

	def __str__(self):
		print("hello")
		self.__say_hello()
		return "密码%s"%self.__password
	
	#该方法在外部不能被调用，只能在内部被调用
	def __say_hello(self):
		print(self.__password)

	def get_password(self):
		return self.__password

u1=User("123456")
#print(u1.get_password())
print(u1)


