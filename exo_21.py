tuple1=[(10,20,40),(40,50,60),(70,80,90)]

def change(tuple0,a):
    for i in tuple0:
        if i is tuple0[-1][-1]:
            tuple0.remove(i)
            tuple0=tuple0.append(a)
        
        
    return tuple0

print(change(tuple1,100))