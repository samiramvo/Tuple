def ident(liste):
    som=0
    for i in liste:
       
        if isinstance(i,tuple):
           break
        som+=1 
       
    return som

print(ident([1,2,3,"Sak",(1,2),6,0]))    