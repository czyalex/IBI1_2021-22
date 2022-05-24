import os
os.chdir('C:/Users/80753/IBI1_2021-22/IBI1_2021-22/Practical8')
with open('Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa','r') as fa:
    dict1={}
    for line in fa:
        if line.startswith('>'):
            name=line
            dict1[name]=''
        else:
            dict1[name]+=line.replace('\n', '')
            pass
        pass
    pass
# read the original file into a dictionary that the key is the name and description and the values is the sequence
num=[]
name_list1=[]
name_list=[]
value_list=[]
len_list=[]
for values in dict1.values():
    n = values.count('GAATTC')
    num.append(n)
    len1 = str(len(values))
    len_list.append(len1)
    value_list.append(values)
    pass
# find out which sequence has GAATTC
for key in dict1:
    ind=key.index('gene:')
    name1=key[ind+5:ind+12]
    name_list1.append(name1)
    pass
# find out which sequence has GAATTC
index_list=[]
for index,value in enumerate(num):
    if value==0:
        index_list.append(index)
        pass
    pass
# find out the location of the ID that didn't have GAATTC in the dictionary
for n in index_list[::-1]:
    name_list1.pop(n)
    value_list.pop(n)
    num.pop(n)
    pass
# pop every sequence that did not contain GAATTC

name_list=list(zip(name_list1,len_list))
final_dict=dict(zip(name_list,value_list))
output_fa = open('C:/Users/80753/IBI1_2021-22/IBI1_2021-22/Practical8/cut_genes1.fa','w')
for key1,value1 in final_dict.items():
    key2=','.join(key1)
    output_fa.write(str(key2))
    output_fa.write('\r\n')
print('finish')
# write them in the new fa file