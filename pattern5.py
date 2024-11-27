n=int(input())

for row in range(1,n+1):
    dum=row
    for st in range(1,n+1):
        print(chr(dum+64),end=' ')
        if row%2==0:
          dum+=2
        else:
           dum+=1
    print()