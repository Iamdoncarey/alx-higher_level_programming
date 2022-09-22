#!/usr/bin/python3

if __name == __"main":
	"""Print the sum, difference, product, quotient of 10 and 5"""
	from calculator_1 import add, sub, mul, div
	
	a = 10
	b = 5
	
	print("{} + {} = {}".format(a, b, add(a, b)))
	print("{} - {} = {}".format(a, b, sub(a, b)))
	print("{} * {} = {}".format(a, b, mul(a, b)))
	print("{} / {} = {}".format(a, b, div(a, b)))
	print(res_add)
	print(res_sub)
	print(res_mul)
	print(res_div)
