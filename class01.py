class Car:
  def start(self):
    print('车辆启动')
  def print_car_inf(self):
    print("车的名字是:%s,颜色为:%s"%(self.name,self.color))
car1=Car()
car1.name="迈腾"
car1.color="金色"
car1.start()
car1.print_car_inf()

