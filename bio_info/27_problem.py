def Breakpoint(arr):
    answ = 0
    for i in range(len(arr)-1):
        if(arr[i+1] - arr[i] != 1):
            answ += 1
    return answ

s = input()
s = s[1:]
s = s[:-1]
arr = list(map(int, s.split(' ')))
print(Breakpoint(arr))