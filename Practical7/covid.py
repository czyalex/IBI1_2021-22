import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
os.chdir('C:/Users/80753/IBI1_2021-22/IBI1_2021-22/Practical7')
# importing the.csv fileworks
covid_data = pd.read_csv('full_data(2).csv')
#  showing the first and third columns from rows 10-20 (inclusive)
my_columns = [True, False, True, False, False, False]
print(covid_data.iloc[10:21,my_columns])
# used a Boolean to show“total cases” for all rows corresponding to Afghanistan
columns=[False,True,False,False,True,False]
print(covid_data.loc[ covid_data[ "location"]=='Afghanistan',columns])
# computed the mean number of new cases and new deaths in China.
china_new_data=covid_data.loc[covid_data['location']=='China',['date','new_cases','new_deaths']]
mean_China_newcases=china_new_data['new_cases'].mean()
mean_China_newdeaths=china_new_data['new_deaths'].mean()
print(mean_China_newdeaths)
print(mean_China_newcases)
pro=mean_China_newdeaths/mean_China_newcases
# computed the mean number of new cases and new deaths in China.
print('the proportion of new cases that kill the infected person is%.2f%%'%(pro*100))
new_cases=covid_data.loc[covid_data['location']=='China','new_cases']
new_deaths=covid_data.loc[covid_data['location']=='China','new_deaths']
china_dates=covid_data.loc[covid_data['location']=='China','date']
C=list(covid_data.loc[covid_data['location']=='China','date'])
A=list(new_cases)
B=list(new_deaths)
data={'new_cases':A,'new_deaths':B}
df=pd.DataFrame(data)
df.plot.box(showfliers=False)
plt.title('new cases and new deaths in China')
plt.ylabel('number')
plt.show()
# plotted both new cases and new deaths in China over time
plt.plot(C,A, 'bo')
plt.plot(C,B, 'ro')
plt.xlabel('date')
plt.ylabel('number')
plt.title('new cases and new deaths in China over time')
plt.xticks(china_dates.iloc[0:len(china_dates):4],rotation=-90)
plt.show()
# answer the question
Spain_dates=covid_data.loc[covid_data['location']=='Spain','date']
Spain_total_cases=covid_data.loc[covid_data['location']=='Spain','total_cases']
Spain_new_cases=covid_data.loc[covid_data['location']=='Spain','new_cases']
plt.plot(Spain_dates,Spain_new_cases,'ro')
plt.plot(Spain_dates,Spain_total_cases,'bo')
plt.xlabel('date')
plt.ylabel('number')
plt.title('new cases and total cases developed over time in Spain')
plt.xticks(Spain_dates.iloc[0:len(Spain_dates):4],rotation=-90)
plt.show()



