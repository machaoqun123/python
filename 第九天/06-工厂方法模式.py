class Person(object):
	
	def __init__(self,name):
		self.name=name

	def work(self):
		print(self.name+"开始工作了")
		#person完成work，需要使用一把斧头

		#在原始社会，人需要一把石斧
		#axe = StoneAxe("花岗岩斧头")
		#使用钢铁的斧头
		#axe = SteelAxe("大马革钢斧头")
		#axe.cut_tree()
		
		#已经有工厂
		factory = Steel_Axe_Factory()
		axe = factory.create_axe() 
		axe.cut_tree()


class Axe(object):
	
	def __init__(self,name):
		self.name=name

	def cut_tree(self):
		print("%s斧头开始砍树"%self.name)


class StoneAxe(Axe):
	
	def cut_tree(self):
		print("使用石头做的斧头砍树")


class SteelAxe(Axe):

	def cut_tree(self):
		print("使用钢铁做的斧头砍树")
	

#工厂类
class Factory(object):
	#生产斧头，根据用户指定的类型来生产	
	def create_axe(self):
		pass


class Stone_Axe_Factory(Factory):
	
	def create_axe(self):
		return StoneAxe("花岗岩斧头")


class Steel_Axe_Factory(Factory):
	
	def create_axe(self):
		return SteelAxe("加爵斧头")


p = Person("zs")
p.work()
