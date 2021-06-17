import numpy as np

def answ(v, w, s):
    v_answ = []
    w_answ = []
    sigma = 5
    i, j = len(v), len(w)
    while (i > 0 and j > 0):
        if s[i, j] - BLOSUM62[dict[v[i-1]], dict[w[j-1]]] == s[i-1,j-1]:
            v_answ.append(v[i-1])
            w_answ.append(w[j-1])
            i = i - 1
            j = j - 1
        elif s[i,j] + sigma == s[i,j-1]:
            v_answ.append("-")
            w_answ.append(w[j-1])
            j = j - 1
        elif s[i,j] + sigma == s[i-1,j]:
            v_answ.append(v[i-1])
            w_answ.append("-")
            i = i - 1

    if j > 0:
        while j > 0:
            v_answ.append("-")
            w_answ.append(w[j - 1])
            j = j - 1

    if i > 0:
        while i > 0:
            v_answ.append(v[i-1])
            w_answ.append("-")
            i = i - 1
    return v_answ[::-1], w_answ[::-1]
def LCSBackTrack(v, w):
    n = len(v)
    m = len(w)
    s = np.zeros((n + 1, m + 1))
    Backtrack = np.zeros((n + 1, m + 1))
    sigma = 5
    for i in range(1, n+1):
        s[i][0] = -i*sigma
    for i in range(1, m+1):
        s[0][i] = -i*sigma

    for i in range(1, n+1):
        for j in range(1, m+1):
            s[i, j] = max(s[i - 1, j] - sigma, s[i, j - 1] - sigma, s[i - 1, j - 1] + BLOSUM62[dict[v[i-1]], dict[w[j-1]]])
            if s[i, j] == s[i-1, j] - sigma:
                Backtrack[i, j] = 1
            elif s[i, j] == s[i, j - 1] - sigma:
                Backtrack[i, j] = 2
            elif s[i, j] == s[i-1, j-1] + BLOSUM62[dict[v[i-1]], dict[w[j-1]]]:
                Backtrack[i, j] = 3

    return s[n, m], s

def OutputLCS(backtrack, v, i, j):
    if i == 0 or j == 0 :
        return ""
    if backtrack[i, j] == 1:
        return OutputLCS(backtrack, v, i - 1, j)

    elif backtrack[i, j] == 2:
        return OutputLCS(backtrack, v, i, j - 1)
    else:
        return OutputLCS(backtrack, v, i - 1, j - 1) + v[i-1]

f = open('BLOSUM62.txt', 'r')
BLOSUM62 = np.zeros((20, 20))
for i, line in enumerate(f):
    if (i == 0):
        dict = {}
        keys= line.split("  ")
        keys[19]='Y'
        for j, key in enumerate(keys):
            dict[key]=j
    else:
        ind = 0
        mass = line[1:].split(" ")
        for j in range(len(mass)):
            if(mass[j]!=''):
                BLOSUM62[i-1][ind] = int(mass[j])
                ind+=1

v = input()
w = input()
score, s = LCSBackTrack(v, w)
str1, str2 = answ(v,w,s)
print(int(score))
print(''.join(str1))
print(''.join(str2))




