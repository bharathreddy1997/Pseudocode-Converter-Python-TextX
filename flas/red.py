# Function for nth Fibonacci number
class test(object):

	def Fibonacci(proglang):
		if proglang<0:
			print("Incorrect Input")
		# First Fibonacci number is 0
		elif proglang==1:
			return 0
		# Second Fibonacci number is 1
		elif proglang==2:
			return 1
		else:
			return test.Fibonacci(proglang-1)+test.Fibonacci(proglang-2)
