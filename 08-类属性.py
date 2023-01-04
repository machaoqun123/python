class User(object):
	name="zs"##公共的类属性
	__password="123456"##私有的类属性

	def __init__(self,sex,username,age):
		self.sex=sex
		self.username=username ##对象属性
		self.__age=age
		self.password=User.__password
	def __str__(self):
		return User.__password

class QQ_User(User):
	pass	
#每个对象都可以有不同的属性
u = User("男","goldbin","18")
print(QQ_User.name)##name是从父类继承过来的，name属于类属性，可以直接通过类访问，也可以通过类的对象访问。
print(u.name)##对象属性和类属性名字一样。如果通过对象来访问会选择对象的属性。
print(User.name)
print(u)
#类属性修改,类属性只能通过类来修改
User.name="ww"##真正的类属性修改
u.name="ww"##本质上没有修改类属性，仅仅是给该对象定义了一个对象属性name，并且赋值为"ww".
print(u.name)
print(User.name)
print(u.password)
#print(User.__password)##报错，私有属性，不能在外部被使用


