'''
CYCLOPEPTIDESEQUENCING(Spectrum)
        Peptides ← a set containing only the empty peptide
        while Peptides is nonempty
            Peptides ← Expand(Peptides)
            for each peptide Peptide in Peptides
                if Mass(Peptide) = ParentMass(Spectrum)
                    if Cyclospectrum(Peptide) = Spectrum
                        output Peptide
                    remove Peptide from Peptides
                else if Peptide is not consistent with Spectrum
                    remove Peptide from Peptides
'''
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

def composition(arr):
    answ = set()
    for string in arr:
        pr = list(string)
        s=''
        for i in pr:
           s+=str(weight[i])+'-'
        s=s[:len(s)-1]
        answ.add(s)

    return answ

weight = {'G': 57, 'A': 71, 'S': 87, 'P': 97, 'V': 99, 'T': 101, 'C': 103, 'I': 113, 'L': 113, 'N': 114, 'D': 115, 'K': 128, 'Q': 128, 'E': 129, 'M': 131, 'H': 137, 'F': 147, 'R': 156, 'Y': 163, 'W': 186}
data = "".join(open('StringReconstructionProblem.txt')).split()
data = list(map(int, data))
print(" ".join(composition(CYCLOPEPTIDESEQUENCING(data))))