class Animal:
	
	def __init__(self):
		print("动物的初始化")
		#self.name="动物" ## 如果变为私有属性self.__name,则不能通过init方法继承属性。
		self.color="yellow"
	def eat(self):
		print("动物的颜色:%s"%self.color) ## 子类无法继承父类私有的
		print("-----吃饭-----")
	def sleep(self):
		print("-----睡觉-----")

class Dog(Animal):
	
	#init和父类的init名字一样，所以叫方法的重写
	def __init__(self,name):
		super().__init__() ##主动调用父类的init方法
		self.name=name
	def shout(self):
		print("-----旺旺-----")


class Cat(Animal):
	# 如果注释掉Cat类的init方法，则Cat类继承父类的init方法，即有name属性；如不注释掉，则Cat并不继承父类的属性，进而报错。	
	#def __init__(self):
		#print("猫的初始化")
	def catch(self):
		print("-----捉鼠-----")


class ZangAo(Dog):

	def fight(self):
		print("-----战斗-----")


dog = Dog("小白") ##如何子类中对某个方法重写了，优先调用子类自己本身的方法
#虽然init方法重写了，可是还想自动调用父类的init方法，在子类重写init方法中重写一行代码即可实现。
print(dog.name)
print(dog.color)
dog.eat()
cat = Cat()
#print(cat.name)
cat.eat()

zang = ZangAo("藏獒")
zang.eat()

