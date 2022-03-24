name=input('please enter your name:')
marks=[45,36,86,57,53,92,65,45]

marks.sort()
print(marks) #list of sorted values
mark_origin=[45,36,86,57,53,92,65,45]
import numpy as np
average_marks=np.mean(mark_origin)
print(average_marks)
if average_marks<60:
    print('sorry, you didnt pass the exam')
    pass
else:
    print('congratulation, you pass the exam')
    pass
'''
below is the boxplot
'''
import matplotlib.pyplot as plt
plt.boxplot(mark_origin,patch_artist=True,showmeans=True)
plt.xlabel(name)
plt.ylabel('scores')
plt.show()

