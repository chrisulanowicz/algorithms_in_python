stored = [0,1]
def fibonacci(num):
	if len(stored) > num:
		print stored[num]
		return stored[num]
	for i in range(len(stored),num+1):
		stored.append(stored[i-1]+stored[i-2])
	print stored[num]
	return stored[num]

fibonacci(6)

# [0,1,1,2,3,5,8,13]

def fibonacci2(num):
	if num < 2:
		print num
		return num
	fib1 = 0
	fib2 = 1
	for i in range(2, num+1):
		fib1, fib2 = fib2, fib1+fib2
	print fib2
	return fib2

fibonacci2(6)