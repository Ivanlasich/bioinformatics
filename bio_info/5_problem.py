nucleotides = ['A','C','G','T']


def NumberToSymbol(index):
    if index == 0:
        return "A"
    if index == 1:
        return "C"
    if index == 2:
        return "G"
    if index == 3:
        return "T"

def NumberToPattern(index, k):
    if (k == 1):
        return NumberToSymbol(index)
    prefixIndex = int(index) // 4
    r = int(index) % 4
    symbol = NumberToSymbol(r)
    PrefixPattern = NumberToPattern(prefixIndex, k - 1)
    return PrefixPattern + symbol


def PatternToNumber(Pattern):
    if (Pattern==''):
        return 0
    else:
        symbol = Pattern[-1]
        Prefix = Pattern[:-1]
        return 4 * PatternToNumber(Prefix) + SymbolToNumber(symbol)

def SymbolToNumber(symbol):
    if (symbol == 'A'):
        return 0
    if (symbol == 'C'):
        return 1
    if (symbol == 'G'):
        return 2
    if (symbol == 'T'):
        return 3


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


def hamming_distance(str1, str2):
    answ = 0
    for s1, s2 in zip(str1, str2):
        if (s1 != s2):
            answ += 1
    return answ

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


def FrequentWordsWithMismatches(Text, k, d):
    FrequentPatterns = set()
    Neighborhoods = []
    for i in range(len(Text) - k + 1):
        Neighborhoods.append(Neighbors(Text[i:i+k],d))
        Neighborhoods.append(Neighbors(reverse(Text)[i:i+k], d))

    NeighborhoodArray = []
    for i in Neighborhoods:
        for j in i:
            NeighborhoodArray.append(j)

    Count = [0 for i in range(len(NeighborhoodArray))]
    Index = [0 for i in range(len(NeighborhoodArray))]

    for i in range(len(NeighborhoodArray)):
        Pattern = NeighborhoodArray[i]
        Index[i] = PatternToNumber(Pattern)
        Count[i] = 1
    SortedIndex = Index
    SortedIndex.sort()
    for i in range(len(NeighborhoodArray) - 2 + 1):
        if SortedIndex[i] == SortedIndex[i + 1]:
            Count[i + 1] = Count[i] + 1
    maxCount = max(Count)
    for i in range(len(NeighborhoodArray)):
        if Count[i] == maxCount:
            Pattern = NumberToPattern(SortedIndex[i], k)
            FrequentPatterns.add(Pattern)
    return FrequentPatterns






Text = 'CGACTCACGACTCACCAGCGGCGTTCACTCCGTTCACTCCCGACTCAGTTCACTCCAATCTCACGACTCACGACTCACGTATTTCGGTTCACTCCCGACTCAAATCTCACGTATTTCGAATCTCACGTATTTCGAATCTCACGTATTTCGCGTATTTCGCGACTCACGTATTTCGCGACTCACGTATTTCGAATCTCACCAGCGGCCGTATTTCGCGTATTTCGCGACTCACCAGCGGCCGACTCACGTATTTCGCCAGCGGCCCAGCGGCGTTCACTCCCGACTCAGTTCACTCCAATCTCACGTATTTCGAATCTCACGTATTTCGGTTCACTCCCGTATTTCGCGACTCACGACTCAAATCTCAAATCTCACGACTCAGTTCACTCCCGTATTTCGCCAGCGGCCCAGCGGCCGTATTTCGAATCTCAAATCTCACGTATTTCGGTTCACTCCGTTCACTCCCCAGCGGCAATCTCACGACTCACGACTCAGTTCACTCCGTTCACTCCCGACTCAAATCTCACGTATTTCGAATCTCACCAGCGGCCGACTCACGTATTTCGCGACTCAGTTCACTCCGTTCACTCCCGTATTTCGAATCTCACGTATTTCGCGTATTTCGAATCTCAGTTCACTCCAATCTCACGACTCAAATCTCACGACTCAAATCTCACGACTCACGTATTTCGGTTCACTCCCGACTCAGTTCACTCCAATCTCAAATCTCAGTTCACTCCCCAGCGGCGTTCACTCCCGTATTTCGCGTATTTCGCCAGCGGCCCAGCGGCAATCTCAAATCTCACGACTCACGACTCAGTTCACTCCCGACTCACCAGCGGCCCAGCGGCCCAGCGGCGTTCACTCCGTTCACTCC'
k = 5
d = 2

print(' '.join(map(str, (FrequentWordsWithMismatches(Text, k, d)))))
