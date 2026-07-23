n=input('enter the number:')
d=len(n)
sum1=sum(int(i)**d for i in n )
if sum1==int(n):
    print('THE NUMBER IS ARMSTRONG NUMBER')
else:
    print('wrong number')