#最普通的列表
motorcycles=['honda','yamaha','suzuki']
print(motorcycles)

#替换列表元素
motorcycles[0]='ducati'
print(motorcycles)

#列表最后添加元素
motorcycles=['honda','yamaha','suzuki']
motorcycles.append('ducati')
print(motorcycles)

#列表插入元素
motorcycles=['honda','yamaha','suzuki']
motorcycles.insert(0,'ducati')
print(motorcycles)

#删除元素（使用del删除后不能继续使用）
motorcycles=['honda','yamaha','suzuki']
print(motorcycles)
del motorcycles[0]
print(motorcycles)

#pop()删除元素
motorcycles=['honda','yamaha','suzuki']
print(motorcycles)
popped_motorcycle=motorcycles.pop()
print(motorcycles)
print(popped_motorcycle)
#pop可选取元素删除（不填就是删除最后一个并留下它的值；删除后还能继续使用）
motorcycles=['honda','yamaha','suzuki']
last_owned=motorcycles.pop(0)
print("The last motorcycle I owned was a "+last_owned.title()+".")

#根据值删除元素
motorcycles=['honda','yamaha','suzuki','ducati']
print(motorcycles)
motorcycles.remove('ducati')
print(motorcycles)

motorcycles=['honda','yamaha','suzuki','ducati']
print(motorcycles)
too_expensive='ducati'
motorcycles.remove(too_expensive)
print(motorcycles)
print("\nA "+too_expensive.title()+" is too expensive for me.")
