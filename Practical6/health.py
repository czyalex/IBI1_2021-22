# It has recently been reported that our health can be, in part, informed by our father’s age
# when we were born. In particular, it seems that health problems increase in frequency with the
# father’s age at the time of the offspring birth.
a=input('please enter your father ages:') #input the age of the father
paternal_age=[30,35,40,45,50,55,60,65,70,75]
age_risk=[1.03,1.07,1.11,1.17,1.23,1.32,1.42,1.55,1.72,1.94]
dictionary=dict(zip(paternal_age,age_risk)) #combine into a dictionary
print(dictionary)
print(dictionary[int(a)])#print the risk of the health problem
'''
draw the scatter plot below
'''
import matplotlib.pyplot as plt
N=10
x=paternal_age
y=age_risk
plt.scatter(x,y,N)
plt.show()




