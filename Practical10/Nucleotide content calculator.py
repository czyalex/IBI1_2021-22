seq=input('please input your sequence:') # inputting the sequences
Nucleotide=['A','G','C','T']

def nucleotide_caculate(nucleotide,seq1):
    seq_valid = seq1.upper() # put all the sequences into upper class
    for n in seq_valid:
        if n not in Nucleotide:
            return False
        pass # if it contains other letter return False
    n=seq_valid.count(nucleotide)
    l=len(seq_valid)
    percentage=n/l
    return '%2f%%' % (percentage * 100)
# find out the percentage of one nucleotide in sequences
print('------------------example------------------------------------')

print(nucleotide_caculate('A',seq))
# please input your sequence:cagtgcatGCATgatcgaTCgaTCgacATGATGaTgcACTAGcatGaTcgaTCgatcgATCaGctagTAGCATgaTgatcgA
# 29.268293%



