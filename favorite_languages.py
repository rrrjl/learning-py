favorite_languages={
	'jen':'python',
	'sarah':'c',
	'edward':'ruby',
	'phil':'python',
	}
	
print("Sarah's favorite language is "+
	favorite_languages['sarah'].title()+
	".")
#列出所有值item()
favorite_languages={
	'jen':'python',
	'sarah':'c',
	'edward':'ruby',
	'phil':'python',
	}

for name, language in favorite_languages.items():
	print(name.title()+"'s favorite language is "+
		language.title()+".")

#遍历所有键key()
favorite_languages={
	'jen':'python',
	'sarah':'c',
	'edward':'ruby',
	'phil':'python',
	}
	
for name in favorite_languages.keys():
	print(name.title())

favorite_languages={
	'jen':'python',
	'sarah':'c',
	'edward':'ruby',
	'phil':'python',
	}
	
friends=['phil','sarah']
for name in favorite_languages.keys():
	print(name.title())
	
	if name in friends:
		print("Hi "+name.title()+
		", I see your favorite language is "+
		favorite_languages[name].title()+"!")


favorite_languages={
	'jen':'python',
	'sarah':'c',
	'edward':'ruby',
	'phil':'python',
	}
	
if 'erin' not in favorite_languages.keys():
	print("Erin, please take our poll!")

#按顺序遍历所有键sort()
favorite_languages={
	'jen':'python',
	'sarah':'c',
	'edward':'ruby',
	'phil':'python',
	}
	
for name in sorted(favorite_languages.keys()):
	print(name.title()+" , thank you for taking the poll.")
	
#遍历字典中的所有值values()
favorite_languages={
	'jen':'python',
	'sarah':'c',
	'edward':'ruby',
	'phil':'python',
	}

print("The following languages have been mentioned:")
for language in favorite_languages.values():
	print(language.title())
	
	
#去除所有值里面重复的	
favorite_languages={
	'jen':'python',
	'sarah':'c',
	'edward':'ruby',
	'phil':'python',
	}

print("The following languages have been mentioned:")
for language in set(favorite_languages.values()):
	print(language.title())
