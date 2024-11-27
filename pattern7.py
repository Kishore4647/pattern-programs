n=int(input())
stars=0
for row in range(1,n+1):
    stars+=row*2
    dum=1
    for st in range(1,stars+1):
        if st==1 and st==n*2:
            print(dum,end="")
            
            
        
