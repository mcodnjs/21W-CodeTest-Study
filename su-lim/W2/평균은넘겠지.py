a = int(input())

for idx in range(a):
    ave = 0
    command = input().split()
    for i in range(len(command)):
        command[i] = int(command[i])
    for i in range(1,command[0]+1):
        ave += command[i]
    ave = ave / command[0]
    tmp_list = sorted(command[1:])
    command = [command[0]] + tmp_list
    idx = 0
    for i in range(1, command[0]+1):
        if(ave < command[i]):
            idx = command[0]-i+1
            break
    answer = idx / command[0] * 100
    answer = round(answer,3)
    print(format(answer, ".3f")+'%')