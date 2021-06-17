nucleotides = ['A','C','G','T']


def NumberToPattern(index, k):
    if (k == 1):
        return NumberToSymbol(index)
    prefixIndex = int(index) // 4
    r = int(index) % 4
    symbol = NumberToSymbol(r)
    PrefixPattern = NumberToPattern(prefixIndex, k - 1)
    return PrefixPattern + symbol



def NumberToSymbol(index):
    if index == 0:
        return "A"
    if index == 1:
        return "C"
    if index == 2:
        return "G"
    if index == 3:
        return "T"

def hamming_distance(str1, str2):
    answ = 0
    for s1, s2 in zip(str1, str2):
        if (s1 != s2):
            answ += 1
    return answ

def SymbolToNumber(symbol):
    if (symbol == 'A'):
        return 0
    if (symbol == 'C'):
        return 1
    if (symbol == 'G'):
        return 2
    if (symbol == 'T'):
        return 3

def PatternToNumber(Pattern):
    if (Pattern==''):
        return 0
    else:
        symbol = Pattern[-1]
        Prefix = Pattern[:-1]
        return 4 * PatternToNumber(Prefix) + SymbolToNumber(symbol)


def Neighbors(Pattern, d):
    if (d == 0):
        return Pattern
    if (len(Pattern)==1):
        return nucleotides
    Neighborhood = []
    SuffixNeighbors = Neighbors(Pattern[1:], d)
    for text in SuffixNeighbors:
        if hamming_distance(Pattern[1:], text) < d:
            for x in nucleotides:
                Neighborhood.append(x + text)
        else: Neighborhood.append(Pattern[0] + text)
    return Neighborhood


def ComputingFrequenciesWithMismatches(Text, k, d):
    FrequenciesArray = [0 for _ in range(4**k)]
    for i in range(len(Text)-k+1):
        Pattern = Text[i:i+k]
        Neighborhood = Neighbors(Pattern, d)
        for ApproximatePattern in Neighborhood:
            j = PatternToNumber(ApproximatePattern)
            FrequenciesArray[j] += 1
    return FrequenciesArray

def MostFrequentWords(Text, k, d):
    answ = []
    FrequencyArray = ComputingFrequenciesWithMismatches(Text, k, d)
    most_fq = max(FrequencyArray)
    for i, elem in enumerate(FrequencyArray):
        if elem == most_fq:
            answ.append(NumberToPattern(i, k))
    return answ




Text = 'TCTACCCCTCTGCCATTCTACCCCTAATCTGAAAATCTGAATGGGAAATCTACCCCTCTGCCATTCTACCCCTAATCTGAAAATCTGAATCTACCCCTTCTATTCCTTGGGAAATCTATTCCTTCTATTCCTTCTATTCCTTGGGAAATCTACCCCTTCTACCCCTAATCTGAAAATCTGAACTGCCATAATCTGAATCTACCCCTCTGCCATAATCTGAATCTACCCCTTGGGAAATCTACCCCTCTGCCATAATCTGAATCTATTCCTTCTATTCCTTCTATTCCTTCTATTCCTCTGCCATTGGGAAATCTACCCCTTGGGAAATGGGAAATCTACCCCTTCTATTCCTTGGGAAATGGGAAACTGCCATAATCTGAATCTATTCCTTGGGAAAAATCTGAATCTATTCCTAATCTGAATGGGAAACTGCCATTGGGAAAAATCTGAAAATCTGAAAATCTGAATGGGAAATCTACCCCTCTGCCATTGGGAAATCTACCCCTAATCTGAATCTATTCCTTGGGAAATCTACCCCTAATCTGAATGGGAAATCTACCCCTTCTATTCCTTCTATTCCTTGGGAAATGGGAAACTGCCATTCTACCCCTCTGCCATTCTACCCCTTCTACCCCTTCTACCCCTTCTACCCCTTGGGAAATCTATTCCTAATCTGAATCTACCCCTCTGCCATTCTACCCCTTCTACCCCTTCTACCCCTTCTACCCCTTGGGAAACTGCCATTCTACCCCTCTGCCATAATCTGAAAATCTGAATGGGAAACTGCCATCTGCCATCTGCCATCTGCCATTCTACCCCTCTGCCAT'
k = 7
d = 3

print(' '.join(map(str, (MostFrequentWords(Text, k, d)))))

