tuple1=(1,2,3,4)
tuple2=(3,5,2,1)
tuple3=(2,2,3,1)
print(tuple(map(sum,zip(tuple1,tuple2,tuple3))))