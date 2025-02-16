#用sort()排序(永久性排序)
cars=['bmw','audi','toyota','subaru']
cars.sort()
print(cars)
#倒序
cars=['bmw','audi','toyota','subaru']
cars.sort(reverse=True)
print(cars)

#用sorted()将列表按特定顺序排列
cars=['bmw','audi','toyota','subaru']
print("Here is the original list:")
print(cars)

print("\nHere is the sorted list:")
print(sorted(cars))

print("\nHere is the original list again:")
print(cars)

#倒着打印列表（永久性）
cars=['bmw','audi','toyota','subaru']
print(cars)

cars.reverse()
print(cars)

#确定列表长度len()
cars=['bmw','audi','toyota','subaru']
len(cars)
