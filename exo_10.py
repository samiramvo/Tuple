tuple1=(1,2,3,1,3,2,4,5,8,"mis","sofa")
def exist(tuple0,a):
    if a in tuple0:
        return True
    else:
        return False

print(exist(tuple1,3))
print(exist(tuple1,"Sis"))