class User:

	def __str__(self):
		return "用户名为:%s,密码为:%s"%(self.username,self.password)
	
	def set_password(self,pw):
		if len(pw)>=6:
			self.password=pw
		else:
			print("密码%s,长度不符合规定"%pw)

u1=User()
u1.username="goldbin"
u1.set_password("123456")
#该方法并不能将密码保护起来
u1.password="123"
print(u1)

