import os
from xml.dom.minidom import parse
import xml.dom.minidom
import matplotlib.pyplot as plt
from copy import deepcopy
path = os.path.abspath('.')
data_path = os.path.join(path,'./go_obo(1).xml')
DOMTree = xml.dom.minidom.parse("go_obo(1).xml")
collection = DOMTree.documentElement
terms = collection.getElementsByTagName("term")
n=0
count1=0
dictionary={}
for term in terms:
    count1+=1
    if term.getElementsByTagName('is_a'):
        length=len(term.getElementsByTagName('is_a'))
        # print(length)
        term_id = term.getElementsByTagName('id')[0].childNodes[0].data
        # print(term_id)
        while n < length:
            is_a_txt=term.getElementsByTagName('is_a')[n].childNodes[0].data
            if is_a_txt not in dictionary:
                dictionary[is_a_txt]=[term_id]
            else:
                dictionary[is_a_txt].append(term_id)
            n+=1
    n=0
print('there are %d term in GO'%(count1))
# print(dictionary['GO:0051048'])
o=0
dictionary_final=deepcopy(dictionary)
lenlist=[]
while o<3:
    for i in dictionary:
        for p in dictionary_final[i]:
            if p in dictionary:
                dictionary_final[i].extend(dictionary[p])
    o+=1
for u in dictionary_final:
            b=(set(dictionary_final[u]))
            dictionary_final[u]=b
# print(dictionary['GO:0051048'])
# print(dictionary_final['GO:0051048'])
for y in dictionary_final:
    length1=len(dictionary_final[y])
    lenlist.append(length1)
# print(lenlist)
count=0
for t in dictionary_final:
    count+=1
for r in range(0,count1-count):
    lenlist.append(0)
from numpy import *
print('the mean of the child nodes in GO is',mean(lenlist))
ID_list=[]
for term in terms:
    defstr = term.getElementsByTagName('defstr')[0].childNodes[0].data
    real_defstr=defstr.upper()
    ID = term.getElementsByTagName('id')[0].childNodes[0].data
    # l = defstr.count('translation')
    l=real_defstr.count('TRANSLATION')
    if l>=1 :
        ID_list.append(ID)
count2=0
final_count_list=[]
final_lsit=[]
for id in ID_list:
    if id in dictionary_final:
        final_lsit.append(dictionary_final[id])
    else:
        count2+=1
for j in range(0,count2):
    final_count_list.append(0)
for h in final_lsit:
    final_count_list.append(len(h))
# print(final_count_list)
print('the mean of the child nodes that related to translation is',mean(final_count_list))
plt.boxplot(lenlist,patch_artist=False,showmeans=True,showfliers=True)
plt.xlabel('the distribution of child nodes across terms')
plt.ylabel('childnodes')
plt.show()
plt.boxplot(final_count_list,patch_artist=False,showmeans=True,showfliers=True)
plt.xlabel('the distribution of child nodes across terms associate with translate')
plt.ylabel('childnodes')
plt.show()
# On average, the ‘translation’ terms contain a greater  of child nodes than the overall Gene Ontology.
