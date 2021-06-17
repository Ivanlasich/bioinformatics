def SubstringsFinding(text, pattern):
    n = len(text)
    k = len(pattern)
    answ = []
    for i in range(0,n - 3*k + 1):
        sub = text[i:i + 3*k]
        arr = check(sub, pattern)
        if (arr!=''):
            answ.append(arr)
    return (answ)

def reverse(str):
    str1 = []
    for i in range(len(str)):
        if str[i] == 'A':
            str1.append('T')
        if str[i] == 'C':
            str1.append('G')
        if str[i] == 'T':
            str1.append('A')
        if str[i] == 'G':
            str1.append('C')
    return ''.join(str1[::-1])

def check(sub, pattern):
    sub_t = sub.replace('T', 'U')
    sub_r = reverse(sub).replace('T', 'U')
    d = ''
    for i,j in enumerate(range(0, len(sub_t), 3)):
        if (not GeneticCode.get(sub_t[j:j + 3])):
            return ''
        elif(GeneticCode.get(sub_t[j:j + 3])== pattern[i]):
            d += sub[j:j+3]
        elif(GeneticCode.get(sub_r[j:j + 3])== pattern[i]):
            d += sub[j:j + 3]
        else:
            return ''

    return d


GeneticCode = {'AAA': 'K', 'AAC': 'N', 'AAG': 'K', 'AAU': 'N', 'ACA': 'T', 'ACC': 'T', 'ACG': 'T', 'ACU': 'T', 'AGA': 'R', 'AGC': 'S', 'AGG': 'R', 'AGU': 'S', 'AUA': 'I', 'AUC': 'I', 'AUG': 'M', 'AUU': 'I', 'CAA': 'Q', 'CAC': 'H', 'CAG': 'Q', 'CAU': 'H', 'CCA': 'P', 'CCC': 'P', 'CCG': 'P', 'CCU': 'P', 'CGA': 'R', 'CGC': 'R', 'CGG': 'R', 'CGU': 'R', 'CUA': 'L', 'CUC': 'L', 'CUG': 'L', 'CUU': 'L', 'GAA': 'E', 'GAC': 'D', 'GAG': 'E', 'GAU': 'D', 'GCA': 'A', 'GCC': 'A', 'GCG': 'A', 'GCU': 'A', 'GGA': 'G', 'GGC': 'G', 'GGG': 'G', 'GGU': 'G', 'GUA': 'V', 'GUC': 'V', 'GUG': 'V', 'GUU': 'V', 'UAA': [], 'UAC': 'Y', 'UAG': [], 'UAU': 'Y', 'UCA': 'S', 'UCC': 'S', 'UCG': 'S', 'UCU': 'S', 'UGA': [], 'UGC': 'C', 'UGG': 'W', 'UGU': 'C', 'UUA': 'L', 'UUC': 'F', 'UUG': 'L', 'UUU': 'F'}
data = "".join(open('StringReconstructionProblem.txt')).split()
#otv1 = "".join(open('answ.txt')).split()
#otv2 = SubstringsFinding(data[0], data[1])
#otv1 = sorted(otv1)
'''
for s1, s2 in zip(otv1, otv2):
    if s1!=s2:
        print(s1)
        print(s2)
'''
print('\n'.join(SubstringsFinding(data[0], data[1])))