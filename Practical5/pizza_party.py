n=0
q=1
while q<=64:  #keep the loop run until 64 slices was cut
    n+=1
    q+=n
    print('we cut %s times, there are %s slice' % (str(n), str(q)))
    pass

print('there are %s slices, it is enough for each member of the class'%(str(q)))
  # pirnt how many cut we use
