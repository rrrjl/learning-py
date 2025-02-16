#not in 指代不包含在列表中
banned_users=['andrew','carolina','david']
user='marie'

if user not in banned_users:
	print(user.title()+", you can post a response if you wish.")


#测试题
car='subaru'
print("Is car=='subaru'? I predict True.")
print(car=='subaru')

print("\nIS car =='audi'? I predict False.")
print(car=='audi')
