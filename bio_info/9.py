import numpy as np
import random
import copy

def hamming_distance(str1, str2):
    answ = 0
    for s1, s2 in zip(str1, str2):
        if (s1 != s2):
            answ += 1
    return answ

def NumberToSymbol(index):
    if index == 0:
        return "A"
    if index == 1:
        return "C"
    if index == 2:
        return "G"
    if index == 3:
        return "T"

def Profile_laplas(mat) :
    Profile = np.ones((len(mat[0]) , 4))
    t_mat = mat.T
    for i in range(len(t_mat)):
        for j in range(len(t_mat[i])):
            if t_mat[i][j]=='A':
                Profile[i][0]+=1
            if t_mat[i][j]=='C':
                Profile[i][1]+=1
            if  t_mat[i][j]=='G':
                Profile[i][2]+=1
            if  t_mat[i][j]=='T':
                Profile[i][3]+=1
    Profile = Profile/(len(mat)+4)
    return Profile.T

def Score(motifs):
    Profiles = Profile_laplas(motifs).T
    consensus = []
    for prof in Profiles:
        maxi = max(prof)
        for i in range(len(prof)):
            if prof[i] == maxi:
                consensus.append(NumberToSymbol(i))
                break;
    consensus = np.array(consensus)
    score = 0
    for motif in motifs:
        score+=hamming_distance(motif, consensus)

    return score

def Bestmotifs(Text, k, motifs):
    Profile_ = Profile_laplas(motifs)
    best_score = 0
    best_mofit = Text[:k]
    for i in range(len(Text)-k+1):
        example = Text[i:i+k]
        score = 1
        for j in range(len(example)):
            if example[j] == 'A':
                score*=Profile_[0][j]
            if example[j] == 'C':
                score*=Profile_[1][j]
            if example[j] == 'G':
                score*=Profile_[2][j]
            if example[j] == 'T':
                score*=Profile_[3][j]
        if (score > best_score):
            best_mofit = example
            best_score = score
    return best_mofit


def GreedyMotifSearch(Dna, k, t):
    BestMotifs = [Dna[i][:k] for i in range(t)]
    for i in range(len(Dna[0])-k+1):
        Motifs = []
        Motif_1 = Dna[0][i:i+k]
        Motifs.append(Motif_1)
        for j in range(1, t):
            Motif_best = Bestmotifs(Dna[j], k, np.array(Motifs))
            Motifs.append(Motif_best)
        if (Score(np.array(Motifs)) < Score(np.array(BestMotifs))):
            BestMotifs = Motifs

    return BestMotifs

def RandomizedMotifSearch(Dna, k, t):
    BestMotifs = []
    for string in Dna:
        n = random.randint(0, len(string) - k)
        BestMotifs.append(string[n:n+k])
    while True:
        Motifs = []
        for j in range(t):
            Motif_best = Bestmotifs(Dna[j], k, np.array(BestMotifs, dtype = 'object'))
            Motifs.append(Motif_best)
        if (Score(np.array(Motifs, dtype = 'object')) < Score(np.array(BestMotifs, dtype = 'object'))):
            BestMotifs = Motifs
        else:
            return BestMotifs

def Best_motifs(Text, k, motifs):
    Profile_ = Profile_laplas(motifs)
    probability = []
    for i in range(len(Text)-k+1):
        example = Text[i:i+k]
        score = 1
        for j in range(len(example)):
            if example[j] == 'A':
                score*=Profile_[0][j]
            if example[j] == 'C':
                score*=Profile_[1][j]
            if example[j] == 'G':
                score*=Profile_[2][j]
            if example[j] == 'T':
                score*=Profile_[3][j]
        probability.append(score)
    '''
    C = sum(probability)
    probability = probability/C
    MAX = max(probability)
    for i in range(len(probability)):
        if (probability[i] == MAX):
            index = i

    return Text[index:index + k]
    '''
    rnd = random.uniform(0, sum(probability))
    current = 0
    for z, bias in enumerate(probability):
        current += bias
        if rnd <= current:
            return Text[z: k + z]

def GibbsSample(Dna, k, t, N):
    Motifs = []
    for string in Dna:
        n = random.randrange(len(string)-k+1)
        Motifs.append(string[n:n+k])

    BestMotifsScore = Score(np.array(Motifs, dtype='object'))
    for j in range(N):
        i = random.randrange(t)
        motifs_ex = Motifs[:i] + Motifs[i + 1:]
        string_tg = Dna[i]
        Motifs[i] = Best_motifs(string_tg, k, np.array(motifs_ex, dtype='object'))
        if (Score(np.array(Motifs, dtype='object')) < BestMotifsScore):
            BestMotifsScore = Score(np.array(Motifs, dtype='object'))
            BestMotifs = Motifs.copy()

    return BestMotifs

k, t, N = list(map(int,input().split()))
data = []
for i in range(t):
    data.append(list(input()))
DNA = np.array(data)


min_score = 20000000000
for i in range(5):
    answ = GibbsSample(DNA, k, t, N)
    if Score(np.array(answ)) < min_score:
        min_score = Score(np.array(answ))
        min_answ = answ
for i in min_answ:
    strt=''
    for j in i:
        strt+=j
    print(strt)
print(min_score)
#print(Score(np.array(answ)))
#print(np.array(Score(answ)))

#print(''.join(map(str, (GreedyMotifSearch(DNA, k, t)))))



'''
k, t = list(map(int,input().split()))
data = []
for i in range(t):
    data.append(list(input()))
test = np.array(data)
print(Score(test))




3 5
GGTGTTCA
GAGGTATG
GAAGTATA
AAGTTTCA
CAGCTCCA
9
'''
'''
EXAMPLE= [['T','A','A','C'],['G','T','C','T'],['A','C','T','A'],['A','G','G','T']]
TEXT = ['C','C','G','G','C','G','T','T','A','G']
print(Best_motifs(TEXT, 4, np.array(EXAMPLE)))
'''