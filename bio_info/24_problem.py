import numpy as np

def answ(v, w, s, i, j):
    v_answ = []
    w_answ = []
    sigma = 5
    while (i > 0 and j > 0):
        if s[i, j] - PAM250[dict[v[i-1]], dict[w[j-1]]] == s[i-1,j-1]:
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
        else:
            break;

    return v_answ[::-1], w_answ[::-1]
def LCSBackTrack(v, w):
    n = len(v)
    m = len(w)
    s = np.zeros((n + 1, m + 1))
    sigma = 5
    for i in range(1, n+1):
        s[i][0] = -i*sigma
    for i in range(1, m+1):
        s[0][i] = -i*sigma

    for i in range(1, n+1):
        for j in range(1, m+1):
            s[i, j] = max(0, s[i - 1, j] - sigma, s[i, j - 1] - sigma, s[i - 1, j - 1] + PAM250[dict[v[i-1]], dict[w[j-1]]])

    score = 0
    for k in range(n + 1):
        for t in range(m + 1):
            if score < s[k][t]:
                score = s[k][t]
                i = k
                j = t

    v_answ, w_answ = answ(v, w, s, i, j)
    return s[i,j], v_answ, w_answ

def OutputLCS(backtrack, v, i, j):
    if i == 0 or j == 0 :
        return ""
    if backtrack[i, j] == 1:
        return OutputLCS(backtrack, v, i - 1, j)

    elif backtrack[i, j] == 2:
        return OutputLCS(backtrack, v, i, j - 1)
    else:
        return OutputLCS(backtrack, v, i - 1, j - 1) + v[i-1]

f = open('PAM250.txt', 'r')
PAM250 = np.zeros((20, 20))
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
                PAM250[i-1][ind] = int(mass[j])
                ind+=1


v = input()
w = input()
score, str1, str2 = LCSBackTrack(v, w)
print(int(score))
print(''.join(str1))
print(''.join(str2))




