seq=input('please input your sequence:')
Nucleotide=['A','G','C','T']

def nucleotide_caculate(nucleotide,seq1):
    seq_valid = seq1.upper()
    for n in seq_valid:
        if n not in Nucleotide:
            return False
        pass
    n=seq_valid.count(nucleotide)
    l=len(seq_valid)
    percentage=n/l
    return '%2f%%' % (percentage * 100)
print('------------------example------------------------------------')

print(nucleotide_caculate('A',seq))
# please input your sequence:cagtgcatGCATgatcgaTCgaTCgacATGATGaTgcACTAGcatGaTcgaTCgatcgATCaGctagTAGCATgaTgatcgA
# 29.268293%



