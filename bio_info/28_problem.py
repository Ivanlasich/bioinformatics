def split_into_cycles(str):
    return [s[:-1].split() for s in str.split('(')]

s1 = input()
s2 = input()
print(s1.split('('))
p = split_into_cycles(s1)
q = split_into_cycles(s2)
print(p)
print(q)