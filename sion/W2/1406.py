import sys

input_str = input()
m = int(input())

curr = len(input_str)
for _ in range(m):
  command = sys.stdin.readline().strip()
  if len(command) > 1: # P $
    input_str = input_str[:curr] + command.split()[1] + input_str[curr:]
    curr += 1

  else:
    if (command == 'L'):
      if (curr == 0): continue
      else: curr -= 1
    elif (command == 'D'):
      if (curr == len(input_str)): continue
      else: curr += 1
    elif (command == 'B'):
      if (curr == 0): continue
      else:
        input_str = input_str[:curr-1] + input_str[curr:]
        curr -= 1

print(input_str)
