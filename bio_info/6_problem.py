import numpy as np

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

def Profile(mat):
    Profile = np.zeros((len(mat[0]) , 4))
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
    Profile = Profile/(len(mat))
    return Profile.T

def Score(motifs):
    Profiles = Profile(motifs).T
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
    Profile_ = Profile(motifs)
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

k, t = list(map(int,input().split()))
data = []
for i in range(t):
    data.append(list(input()))
DNA = np.array(data)
answ = GreedyMotifSearch(DNA, k, t)
for i in answ:
    strt=''
    for j in i:
        strt+=j
    print(strt)


#print(''.join(map(str, (GreedyMotifSearch(DNA, k, t)))))
'''

k, t = list(map(int,input().split()))
data = []
for i in range(t):
    data.append(list(input()))
test = np.array(data)
print(Score(test))


'''
'''

3 5
GGCGTTCAGGCA 
AAGAATCAGTCA 
CAAGGAGTTCGC 
CACGTCAATCAC 
CAATAATATTCG
'''
