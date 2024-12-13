n=5
stars=1
space=n-1
for row in range(1,n+1):
    dum=1
    for sp in range(1,space+1):
        print(' ',end='')
    for st in range(1,stars+1):
        print(dum,end='')
        if st>=row:
            dum-=1
        else:
            dum+=1
            
    print()
    stars+=2
    space-=1