class A:
	def test(self):
		print("A-----test()")


class B:
	def test(self):
		print("B-----test()")


class C(A,B):
	def test1(self):
		print("C-----test1()")


c = C()
#打印优先级
print(C.__mro__)
c.test()
