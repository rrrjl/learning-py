squares=[]
for value in range(1,11):
	square=value**2
	squares.append(square)
	
	print(squares)

#简化版
squares=[]
for value in range(1,11):
	squares.append(value**2)
	
	print(squares)


#处理数字列表的函数（直接用python去写代码）
digits=[1,2,3,4,5,6,7,8,9,0]
min(digits)
max(digits)
sum(digits)

squares=[value**2 for value in range(1,11)]
print(squares)
