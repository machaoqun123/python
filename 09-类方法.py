class A(object):
	name="zs"	
	def test1(self):
		print("-----A的test1方法")
	
	@classmethod##类方法一定要在方法的上面加上一个修饰器,类方法的参数cls，代表当前的类
	def test2(cls):
		#A.name="ww"##此种也可以实现修改类属性，可用于实例方法中。
		cls.name="ww"##正规写法
		print("-----A的test2方法")

	@staticmethod##静态方法，属于类的，没有默认传递的参数。可以通过类的对象调用，也可以通过类名调用
	def test3():
		A.name="ls"
		print("-----A的test3静态方法")

a = A()
a.test2()
A.test2()
A.test3()
print(A.name)
