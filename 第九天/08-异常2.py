a="123"
f=None
try:
	f=open("text.txt")
	try:
		content=f.read()
		content.index("hadoop")
	except ValueError as ex:
		print(ex)
	finally:
		print("最里面的finally")
except FileNotFoundError as ex:
	print(ex)
else:##没有异常的情况会自动执行的代码
	print("else")
finally:##最重要执行的代码，不管前面是否出现exception
	print("finally")
	if f:
		f.close()
	
