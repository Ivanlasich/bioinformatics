def hamming_distance(str1, str2):
    answ = 0
    for s1, s2 in zip(str1, str2):
        if (s1 != s2):
            answ += 1
    return answ


def DistanceBetweenPatternAndStrings(Pattern, Dna):
    k = len(Pattern)
    distance = 0
    for string in Dna:
        HammingDistance = float('inf')
        for i in range(len(string)-k+1):
            example = string[i:i + k]
            if HammingDistance > hamming_distance(Pattern, example):
                HammingDistance = hamming_distance(Pattern, example)
        distance = distance + HammingDistance
    return distance

pattern = list(input())
data = input().split(' ')
DNA = [list(string) for string in data]
#print(DNA)

print(DistanceBetweenPatternAndStrings(pattern, DNA))

