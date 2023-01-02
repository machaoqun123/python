class User:

	def __init__(self,pw):
		if len(pw)>=6:
			self.__password=pw
		else:
			print("密码%s不符合规定"%pw)

	def print_pw(self):
		return self.__password

u1=User("123456")
pw=u1.print_pw()
print(pw)
