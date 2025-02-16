sandwich_orders = ['pastrami','tuna','pastrami','cheese', 'hams',
					'pastrami']
finished_sandwiches = []

while sandwich_orders: 
	current_sandwich = sandwich_orders.pop()

	print("I made your " + current_sandwich+" sandwiches.")
	finished_sandwiches.append(current_sandwich)
print("\nThe pastrami sandwiches have been sold out.")
	
while 'pastrami' in finished_sandwiches:
 finished_sandwiches.remove('pastrami') 
	
print("\nThe following sandwiches have been finished:")
for finished_sandwich in finished_sandwiches:
	print(finished_sandwich)
