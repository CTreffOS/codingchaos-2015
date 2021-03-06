import sys

def main(limit):
	for i in range(1, limit + 1):
		if i % 3 == 0 and i % 5 == 0:
			print('FizzBuzz')
		elif not i % 3:
			print('Fizz')
		elif not i % 5:
			print('Buzz')
		else:
			print(i)
	pass

if __name__ == "__main__":
	if len(sys.argv) < 2:
		raise Exception("argument missing")
	limit = int(sys.argv[1])
	main(limit) 