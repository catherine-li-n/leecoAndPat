#  -*-coding utf-8-*-
import numpy as np

def find_wolves(N, statements):
	#i, j
	for i in range(1, N+1):
		for j in range(i+1, N+1):
			a = list(np.ones(N+1, dtype=int))
			a[i] = a[j] = -1
			liar = []
			for k in range(1, N+1):
				if (a[abs(statements[k])] * statements[k]) < 0:
					liar.append(k)
			if (len(liar) == 2) and (a[liar[0]]+a[liar[1]] == 0):
				print("%d %d"%(i,j))
				return 0
	print("No Solution")
	return 0

if __name__ == "__main__":
	statements = [0,]
	N = int(input())
	for i in range(1,N+1):
		statement=int(input())
		statements.append(statement)
	find_wolves(N, statements)
	