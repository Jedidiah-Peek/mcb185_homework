import sys
import gzip
import json


output = []
with gzip.open(sys.argv[1], 'rt') as data:
	info = []
	for line in data:
		info.append(line)
	for a in range(len(info)):
		if info[a].split()[0] == 'ID':
			output.append({})
			output[-1]['id'] = info[a].split()[1]
			name = 0
			b = 4
			row = []
			while name != 'XX':
				row.append({})
				row[-1]['A'] = info[a+b].split()[1]
				row[-1]['C'] = info[a+b].split()[2]
				row[-1]['G'] = info[a+b].split()[3]
				row[-1]['T'] = info[a+b].split()[4]
				b += 1
				name = info[a+b].split()[0]
			output[-1]['pwm'] = row
	print(json.dumps(output, indent=4))