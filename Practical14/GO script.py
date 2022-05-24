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
# output a dictionary that key is the father nodes and the values is the primary children nodes as a list
print('there are %d term in GO'%(count1))
# print(dictionary['GO:0051048'])

dictionary_final=deepcopy(dictionary) # use copy to create a new dict that is used to add the secondary children nodes
lenlist=[]
'''range() can be any figure that greater than 100, it is used to keep the loop run and if the loop get all the 
 child nodes it will break itself'''
for f in range(100): # add the subsequent children nodes into the new dict
    dictionary_test=deepcopy(dictionary_final)
    for h in dictionary_final:
        a = (set(dictionary_test[h]))  # use set to remove the replicate value in every dictionary values
        dictionary_test[h] = a
    for i in dictionary:
        for p in dictionary_final[i]:
            if p in dictionary:
                dictionary_final[i].extend(dictionary[p])
    dictionary_test1 = deepcopy(dictionary_final)
    for g in dictionary_final:
        c = (set(dictionary_test1[g]))  # use set to remove the replicate value in every dictionary values
        dictionary_test1[g] = c
    if dictionary_test1==dictionary_test: # if nothing new was added into the dictionary_final it will break the loop
        break


for u in dictionary_final:
            b=(set(dictionary_final[u])) # use set to remove the replicate value in every dictionary values
            dictionary_final[u]=b
# print(dictionary['GO:0051048'])
# print(dictionary_final['GO:0051048'])
for y in dictionary_final:
    length1=len(dictionary_final[y])
    lenlist.append(length1)
#  find out the amount of children nodes in every term that has children nodes
count=0
for t in dictionary_final:
    count+=1
for r in range(0,count1-count):
    lenlist.append(0)
# for some terms that did not have children nodes input 0 into the list
from numpy import *
print('the mean of the child nodes in GO is',mean(lenlist))
ID_list=[]
for term in terms:
    defstr = term.getElementsByTagName('defstr')[0].childNodes[0].data
    real_defstr=defstr.upper() # use upper class to avoid miscount
    ID = term.getElementsByTagName('id')[0].childNodes[0].data
    # l = defstr.count('translation')
    l=real_defstr.count('TRANSLATION') # use upper class to avoid miscount
    if l>=1 :
        ID_list.append(ID)
# find out the term that its defstr related to translation
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
# output the list of children nodes of terms that related to translation
# print(final_count_list)
print('the mean of the child nodes that related to translation is',mean(final_count_list))
# output the boxplot of the two values
plt.grid(True)
plt.title('the distribution of child nodes without outliers')
plt.boxplot([lenlist,final_count_list],patch_artist=True,showmeans=True,showfliers=False,meanline=True,labels=
[' all terms','  terms associate with translation'])
plt.ylabel('childnodes')
plt.show()
plt.grid(True)
plt.title('the distribution of child nodes with outliers')
plt.boxplot([lenlist,final_count_list],patch_artist=False,showmeans=True,showfliers=True,meanline=True,labels=
[' all terms','  terms associate with translation'])
plt.ylabel('childnodes')
plt.show()
# On average, the ‘translation’ terms contain a greater of child nodes than the overall Gene Ontology.
