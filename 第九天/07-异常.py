try:
	a=1
	print(a)
	i = 1/0##此时第三行没有被执行到
	print("hello")
except (NameError,ZeroDivisionError) as ex:##ex代表刚刚捕获的异常对象 
	print(ex)##捕获到异常之后不会再回头执行之前的代码
	
print("word")

