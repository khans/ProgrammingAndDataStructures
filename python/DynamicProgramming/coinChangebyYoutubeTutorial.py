#Source: https://bitbucket.org/trebsirk/algorithms/src/9728989fdff75481cc419593f4189e6e07132287/coinchanging.py?at=master&fileviewer=file-view-default
def change(n, coins_available, coins_so_far):
	if sum(coins_so_far) == n:
		print coins_so_far
		return [coins_so_far]
	elif sum(coins_so_far) > n:
		pass
	elif coins_available == []:
		pass
	else:
		for c in change(n, coins_available[:], coins_so_far+[coins_available[0]]):
			print c
			return [c]
		for c in change(n, coins_available[1:], coins_so_far):
			print c
			return [c]

'''if __name__ == '__main__':
	n = 4
	coins = [1, 2, 10, 25]

	solutions = [s for s in change(n, coins, [])]
	for s in solutions:
		print (s)

	print ('optimal solution:', min(solutions, key=len))
'''
change(4,[1,2],[])