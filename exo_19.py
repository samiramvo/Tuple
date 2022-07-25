liste=[("a",1),("b",2),("c",3)]
dictionnaire={}
for i ,j in liste:
    dictionnaire.setdefault(i,[]).append(j)
print(dictionnaire)