
def chocolate(money,price):
    a=money%price
    b=money//price
    return 'you can buy %d bars of chocolate, and there is %d money left'%(b,a)
c=chocolate(100,6)
print(c)
# you can buy 16 bars of chocolate, and there is 4 money left

