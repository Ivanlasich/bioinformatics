def get_count(n):
    answ = 0
    if (count[n] == -1):
        for i in mass:
            if n - i == 0:
                answ+=1
            if n - i > 0:
                get_count(n-i)
                answ+=count[n - i]
        count[n] = answ


mass = [57, 71, 87, 97, 99, 101, 103, 113, 114, 115, 128, 129, 131, 137, 147, 156, 163, 186]
n = 1377

count = [-1 for i in range(n+1)]
get_count(n)
print(count[-1])
