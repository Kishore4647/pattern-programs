n=5
stars=1
space=n-1

for row in range(1,n+1):
    dum=row
    for space in range(1,space+1):
        print(' ',end='')
    for st in range(1,stars+1):
        print(dum,end='')
        dum-=1
        
    print()
    space-=1
    stars+=1