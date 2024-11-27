n=5
for row in range(1,n+1):
    dum=1
    if row==1 or row==n:
        for col in range(1,n+1):
            print(chr(dum+64),end=' ')
            dum+=1
    else:
        for col in range(1,n+1):
            if col==1:
                print('A',end=' ')
            elif col==n:
                
               print('B',end=' ')
            else:
                print(' ',end=' ')

    
    print()

           