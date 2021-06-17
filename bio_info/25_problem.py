import numpy as np

def insert(str, i):
    return str[:i] + '-' + str[i:]

def answ(backtrack, v, w, u):
    v_answ = v
    w_answ = w
    u_answ = u

    i, j, k = len(v), len(w), len(u)

    while i * j * k != 0:
        if backtrack[i][j][k] == 1:
            i -= 1
            w_answ = insert(w_answ, j)
            u_answ = insert(u_answ, k)
        elif backtrack[i][j][k] == 2:
            j -= 1
            v_answ = insert(v_answ, i)
            u_answ = insert(u_answ, k)
        elif backtrack[i][j][k] == 3:
            k -= 1
            v_answ = insert(v_answ, i)
            w_answ = insert(w_answ, j)
        elif backtrack[i][j][k] == 4:
            i -= 1
            j -= 1
            u_answ = insert(u_answ, k)
        elif backtrack[i][j][k] == 5:
            i -= 1
            k -= 1
            w_answ = insert(w_answ, j)
        elif backtrack[i][j][k] == 6:
            j -= 1
            k -= 1
            v_answ = insert(v_answ, i)
        else:
            i -= 1
            j -= 1
            k -= 1

    while len(v_answ) != max(len(v_answ), len(w_answ), len(u_answ)):
        v_answ = insert(v_answ, 0)
    while len(w_answ) != max(len(v_answ), len(w_answ), len(u_answ)):
        w_answ = insert(w_answ, 0)
    while len(u_answ) != max(len(v_answ), len(w_answ), len(u_answ)):
        u_answ = insert(u_answ, 0)

    return v_answ, w_answ, u_answ


def LCSBackTrack(v, w, u):
    n = len(v)
    m = len(w)
    l = len(u)
    s = np.zeros((n + 1, m + 1, l + 1))
    backtrack = np.zeros((n + 1, m + 1, l + 1))

    for i in range(1, n+1):
        for j in range(1, m+1):
            for k in range(1, l+1):
                score = 0
                if(v[i-1] == w[j-1] == u[k-1]):
                    score = 1
                s[i][j][k] = max(s[i-1][j-1][k-1] + score, s[i-1][j][k], s[i][j-1][k], s[i][j][k-1], s[i-1][j][k-1], s[i][j-1][k-1],  s[i-1][j-1][k])
                if s[i,j,k] == s[i-1][j-1][k-1] + score:
                    backtrack[i][j][k] = 0
                elif s[i,j,k] == s[i-1][j][k]:
                    backtrack[i][j][k] = 1
                elif s[i,j,k] == s[i][j-1][k]:
                    backtrack[i][j][k] = 2
                elif s[i, j, k] == s[i][j][k-1]:
                    backtrack[i][j][k] = 3
                elif s[i, j, k] == s[i-1][j][k-1]:
                    backtrack[i][j][k] = 4
                elif s[i, j, k] == s[i][j-1][k-1]:
                    backtrack[i][j][k] = 5
                elif s[i, j, k] == s[i-1][j][k-1]:
                    backtrack[i][j][k] = 6
    score = s[n][m][l]
    return score, backtrack

v = input()
w = input()
u = input()
score, backtrack = LCSBackTrack(v, w, u)
print(int(score))
str1, str2, str3 = answ(backtrack, v, w, u)
print(str1)
print(str2)
print(str3)




