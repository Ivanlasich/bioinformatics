'''
LEADERBOARDCYCLOPEPTIDESEQUENCING(Spectrum, N)
        Leaderboard ← {0-peptide}
        LeaderPeptide ← 0-peptide
        while Leaderboard is non-empty
            Leaderboard ← Expand(Leaderboard)
            for each Peptide in Leaderboard
                if Mass(Peptide) = ParentMass(Spectrum)
                    if Score(Peptide, Spectrum) > Score(LeaderPeptide, Spectrum)
                        LeaderPeptide ← Peptide
                else if Mass(Peptide) > ParentMass(Spectrum)
                    remove Peptide from Leaderboard
            Leaderboard ← Cut(Leaderboard, Spectrum, N)
        output LeaderPeptide
'''
def LEADERBOARDCYCLOPEPTIDESEQUENCING(Spectrum, N):
    Leaderboard = ['']
    LeaderPeptide = ''
    ParentMass = Spectrum[-1]
    while (Leaderboard!=[]):
        Leaderboard = Expand(Leaderboard)
        Remove = Leaderboard.copy()
        for Peptide in Leaderboard:
            if (Mass(Peptide) == ParentMass):
                if Score(Peptide, Spectrum) > Score(LeaderPeptide, Spectrum):
                    LeaderPeptide = Peptide
            elif Mass(Peptide) > ParentMass:
                Remove.remove(Peptide)
        Leaderboard = Cut(Remove, Spectrum, N)

    return LeaderPeptide

def linear(Peptide):
    p_spectr = []
    p_spectr.append(0)
    for i in range(len(Peptide)):
        s = Peptide[i]
        p_spectr.append(weight[s])
        for j in range(i + 1, len(Peptide)):
            s += Peptide[j]
            p_spectr.append(Mass(list(s)))

    p_spectr = sorted(p_spectr)

    return p_spectr


def Score(Peptide, Spectrum):
    score = 0
    pep_set = {}
    spec_set = {}
    peptide = linear(Peptide)
    for i in peptide:
        if (not pep_set.get(i)):
            pep_set[i] = peptide.count(i)
            spec_set[i] = Spectrum.count(i)
    for i in pep_set:
        score+=min(pep_set[i], spec_set[i])
    return score

def Cut(Leaderboard, Spectrum, N):
    answ = []
    current = []
    for i in Leaderboard:
        current.append((Score(i, Spectrum), i))
    current.sort(reverse=True)
    current = current[:N]
    for i in current:
        answ.append(i[1])
    return answ

def CYCLOPEPTIDESEQUENCING(Spectrum):
    answ = []
    Peptides = ['']
    ParentMass = Spectrum[-1]
    while (Peptides != []):
        Remove = []
        Peptides = Expand(Peptides)
        for Peptide in Peptides:
            if Mass(Peptide) == ParentMass:
                if Cyclospectrum(Peptide, Spectrum) == Spectrum:
                    answ.append(Peptide)
                Remove.append(Peptide)
            elif (not Consistent(Peptide, Spectrum)):
                Remove.append(Peptide)

        for i in range(len(Remove)):
            Peptides.remove(Remove[i])

    return answ

def Expand(Peptides):
    ex_peptides = []
    for i in Peptides:
        for j in weight:
            ex_peptides.append(i+j)
    return ex_peptides

def Mass(Peptide):
    return sum([weight[i] for i in Peptide])

def Cyclospectrum(Peptide, Spectrum):
    cycle = []
    cycle.append(0)
    for i in range(len(Peptide)):
        string = Peptide[i:] + Peptide[:i]
        pattern = ''
        for j in range(len(string)):
            pattern+=string[j]
            cycle.append(Mass(list(pattern)))
    cycle = sorted(cycle)
    cycle = cycle[:len(Spectrum)]
    return cycle

def Consistent(Peptide, Spectrum):
    p_spectr = []
    p_spectr.append(0)
    for i in range(len(Peptide)):
        s = Peptide[i]
        p_spectr.append(weight[s])
        for j in range(i+1, len(Peptide)):
            s += Peptide[j]
            p_spectr.append(Mass(list(s)))

    p_spectr = sorted(p_spectr)

    for i in p_spectr:
        if p_spectr.count(i) > Spectrum.count(i):
            return False
    return True




def composition(arr):
    pr = list(arr)
    s=''
    for i in pr:
        s+=str(weight[i])+'-'
    s=s[:len(s)-1]

    return s

def convert(arr):
    pr = list(arr)
    s = []
    for i in pr:
        s.append(weight[i])
    return sorted(s)


weight = {'G': 57, 'A': 71, 'S': 87, 'P': 97, 'V': 99, 'T': 101, 'C': 103, 'I': 113, 'L': 113, 'N': 114, 'D': 115, 'K': 128, 'Q': 128, 'E': 129, 'M': 131, 'H': 137, 'F': 147, 'R': 156, 'Y': 163, 'W': 186}
data = "".join(open('StringReconstructionProblem.txt')).split()
data = list(map(int, data))
N = data[0]
data = data[1:]
answ = (LEADERBOARDCYCLOPEPTIDESEQUENCING(data, N))
print(composition(answ))
#print('163-114-97-129-97-147-99-71-186-71-113-163-115-71-113-128-103-87-128-101-137')
#print('97-129-97-147-99-71-186-71-113-163-115-71-113-128-103-87-128-101-137-163-114')
#st = '97-129-97-147-99-71-186-71-113-163-115-71-113-128-103-87-128-101-137-163-114'
#print(sorted(list(map(int, st.split('-')))))
#print(data)