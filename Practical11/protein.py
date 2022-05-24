import pandas as pd
with open('C:/Users/80753/IBI1_2021-22/IBI1_2021-22/Practical11/DLX5_human.fa','r') as f:
    protein_human=''
    for line in f:
        if line.startswith('>'):
            pass
        else:
            protein_human+=line.replace('\n', '')
with open('C:/Users/80753/IBI1_2021-22/IBI1_2021-22/Practical11/DLX5_mouse.fa','r') as f:
    protein_mouse=''
    for line in f:
        if line.startswith('>'):
            pass
        else:
            protein_mouse+=line.replace('\n', '')
with open('C:/Users/80753/IBI1_2021-22/IBI1_2021-22/Practical11/RandomSeq(1).fa','r') as f:
    protein_random=''
    for line in f:
        if line.startswith('>'):
            pass
        else:
            protein_random+=line.replace('\n', '')
# input the 3 sequence of protein
df=pd.read_excel('C:/Users/80753/IBI1_2021-22/IBI1_2021-22/Practical11/BLOSUM.xlsx')
# input the BLOSUM xlsx
str="ARNDCQEGHILKMFPSTWYVBZX" # use str to match the columns in BLOSUM
# print(type(str.find('A')))
def protein(seq1,seq2):
    total=0
    zip(seq1,seq2)
    for n,i in zip(seq1,seq2):
        N=str.find(n)
        I=str.find(i)
        q=df.iloc[N,I+1]
        total+=q
        pass
    return total
# this function is used to find out the points of two sequences
def protein_similarity (seq1,seq2):
    edit_distance = 0
    for i in range(len(seq1)):
        if seq1[i]!=seq2[i]:
            edit_distance += 1
    similarity=(len(seq1)-edit_distance)/len(seq1)
    return similarity
# this function is used to find out the similarity of two sequences
print(protein(protein_random,protein_mouse))
print(protein(protein_random,protein_human))
print(protein(protein_human,protein_mouse))
print(protein_similarity(protein_random,protein_mouse))
print(protein_similarity(protein_random,protein_human))
print(protein_similarity(protein_human,protein_mouse))

