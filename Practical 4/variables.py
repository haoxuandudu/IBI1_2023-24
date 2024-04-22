a=40
b=36
c=30
d=a-b
e=b-c
if d>e:
    print("Running only training had a greater improvement on running time.")
elif e > d:
    print("Running and strength training had a greater improvement on running time")
else:
    print("They are equal")
X=True
Y=False
W=(X or Y) and not (X and Y)
print(W)
# Truth table
# X      Y      W
# True   True   True
# True   False  True
# False  True   True  
# False   False False