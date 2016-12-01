# def gen_prime(number):

# 	prime_nos = []
# 	if number < 0:
# 		return "only positive numbers allowed"
# 	if type(number) != "int":
# 		return "Invalid Input!!Only numbers allowed"		

# 	else: 
# 		for val in range(2,number):
# 			div = 0
# 			for num in range(2,val - 1):
# 				if val % num == 0:
# 					div = div + 1
# 			if div == 0:
# 				print val
			
# print gen_prime(-10)
def gen_prime(number):

	prime_nos = []
	if number < 0:
		return "only positive numbers allowed"
	
	if not number >= 2:
		return "Input must be greater than 2"

	if type(number) != int:
		return "Invalid Input!!Only numbers allowed"
	else: 
		for val in range(2,number):
			div = 0
			for num in range(2,val - 1):
				if val % num == 0:
					div = div + 1
			if div == 0:
				prime_nos.append(val)
	return prime_nos

print gen_prime(1000)
