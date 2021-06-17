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
    peptide = Cyclospectrum(Peptide, Spectrum)
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
    if (N > len(current)):
        return [i[1] for i in current]
    else:
        min_score = current[N][0]
        index = N
        for i in range(N, len(current)):
            if (current[i][0] == min_score):
                index = i
            else:
                break;
        current = current[:index]
        for i in current:
            answ.append(i[1])
        return answ

def LEADERBOARDCYCLOPEPTIDESEQUENCING(Spectrum, N, M):
    Leaderboard = [[]]
    LeaderPeptide = []
    ParentMass = Spectrum[-1]
    while (Leaderboard!=[]):
        Leaderboard = Expand(Leaderboard, Spectrum, M)
        Remove = Leaderboard.copy()
        for Peptide in Leaderboard:
            if (Mass(Peptide) == ParentMass):
                if Score(Peptide, Spectrum) > Score(LeaderPeptide, Spectrum):
                    LeaderPeptide = Peptide
            elif Mass(Peptide) > ParentMass:
                Remove.remove(Peptide)
        Leaderboard = Cut(Remove, Spectrum, N)

    return LeaderPeptide

def Expand(Peptides, Spectrum, M):
    new_ex = []
    conv = convolution(Spectrum)
    expand = top_mass(conv, M)
    for i in Peptides:
        for j in expand:
            a = i.copy()
            a.append(j)
            new_ex.append(a)
    return new_ex

def Mass(Peptide):
    return sum(Peptide)

def Cyclospectrum(Peptide, Spectrum):
    cycle = []
    cycle.append(0)
    for i in range(len(Peptide)):
        string = Peptide[i:].copy()
        string.extend(Peptide[:i])
        pattern = 0
        for j in range(len(string)):
            pattern += string[j]
            cycle.append(pattern)
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
    s=''
    for i in arr:
        s+=str(i)+'-'
    s=s[:len(s)-1]

    return s

def convert(arr):
    pr = list(arr)
    s = []
    for i in pr:
        s.append(weight[i])
    return sorted(s)


def get_spectral_convolution_dict(spectrum):
    spectrum = sorted(spectrum)
    convolution_dict = {}
    for i in range(len(spectrum) - 1):
        for j in range(i, len(spectrum)):
            mass = spectrum[j] - spectrum[i]
            if mass < 57 or mass > 200:
                continue
            if mass in convolution_dict:
                convolution_dict[mass] += 1
            else:
                convolution_dict[mass] = 1
    return convolution_dict

def convolution(spectr):
    answ = {}
    spectr = sorted(spectr)
    for i in range(len(spectr)):
        for j in range(i, len(spectr)):
            diff = spectr[j] - spectr[i]
            if (200 >= diff >= 57):
                if(not answ.get(diff)):
                    answ[diff]=1
                else:
                    answ[diff]+=1
    return (answ)

def top_mass(conv, M):
    arr = [(conv[i],i) for i in conv]
    arr.sort(reverse=True)
    max__frq = [arr[i][0] for i in range(len(arr))]
    frq = max__frq[M - 1]
    for i in range(M, len(max__frq)):
        if(max__frq[i] == frq):
            index = i
        else:
            break;
    arr = [arr[i][1] for i in range(len(arr))]

    return arr[:index+1]


weight = {'G': 57, 'A': 71, 'S': 87, 'P': 97, 'V': 99, 'T': 101, 'C': 103, 'I': 113, 'L': 113, 'N': 114, 'D': 115, 'K': 128, 'Q': 128, 'E': 129, 'M': 131, 'H': 137, 'F': 147, 'R': 156, 'Y': 163, 'W': 186}

data = "".join(open('StringReconstructionProblem.txt')).split()
data = list(map(int, data))
M = data[0]
N = data[1]
#print(LEADERBOARDCYCLOPEPTIDESEQUENCING(data[2:], N, M))
print(composition(LEADERBOARDCYCLOPEPTIDESEQUENCING(data[2:], N, M)))