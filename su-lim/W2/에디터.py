from sys import stdin

st1 = list(stdin.readline()[:-1])

command_size = int(stdin.readline())

st2 = []

for i in range(command_size):
	command = stdin.readline()[:-1]

	try:
		if command[0] == 'L':
			st2.append(st1.pop())

		elif command[0] == 'D':
			st1.append(st2.pop())

		elif command[0] == 'B':
			st1.pop()

		else: # P
			st1.append(command[2])
	except:
		pass

st2.reverse()
st2 = st1 + st2
st2 = ''.join( st2 )

print(st2)