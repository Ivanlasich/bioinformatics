def print_(arr):
    print("(", end="")
    for i in range(len(arr)):
        if(i == len(arr)-1):
            if (arr[i] < 0):
                print("{0})".format(arr[i]), end='')
            if (arr[i] > 0):
                print("+{0})".format(arr[i]), end='')
        else:
            if(arr[i] < 0):
                print("{0} ".format(arr[i]), end='')
            if(arr[i]>0):
                print("+{0} ".format(arr[i]), end='')



def GreedySorting(arr):
    negate = lambda x: -x
    get_index = lambda arr, i: list(map(abs, arr)).index(i)
    update = lambda arr, i, j: arr[:i] + list(map(negate, arr[i:j+1][::-1])) + arr[j+1:]
    i = 0
    while(i < len(arr)):
        if i+1 == arr[i]:
            i+=1;
        elif i+1 == negate(arr[i]):
            arr[i] = negate(arr[i])
            print_(arr)
            print()
        else:
            arr = update(arr, i, get_index(arr, i+1))
            print_(arr)
            print()


s = input()
s = s[1:]
s = s[:-1]
arr = list(map(int, s.split(' ')))
GreedySorting(arr)
