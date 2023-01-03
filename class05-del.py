class User:
	def __init__(self):
		print("======对象初始化=======")
	
	def __del__(self):
		print("对象即将要被销毁")

u=User()
u2=u
#del为内建函数
del u ## 第一次仅删除引用，尚存在另一个引用，此时内存不会回收
print("--"*30)
del u2 ## 执行13行时才会调用del方法，引用数为零，才回收内存。
print("=="*30) ## 注释掉13行，则在执行完14行后，调用del方法，因为此时程序已执行完成。
