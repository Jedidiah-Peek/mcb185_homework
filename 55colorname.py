import sys


file = sys.argv[1]
R = int(sys.argv[2])
G = int(sys.argv[3])
B = int(sys.argv[4])

with open(file) as colors:
	best = ''
	closest = 276
	for color in colors:
		distance = 0
		nums = color.split()[2].split(',')
		distance += abs(R - int(nums[0]))
		distance += abs(G - int(nums[1]))
		distance += abs(B - int(nums[2]))
		if distance < closest:
			closest = distance
			best = color.split()[0]

print(best)
