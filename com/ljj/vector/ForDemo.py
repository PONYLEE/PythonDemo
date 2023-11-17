import time

X = []
Y = []
cnt=1000000
for i in range(1,cnt+1):
    X.append(i)

for i in range(1,cnt+1):
    Y.append(i)

print(X)
print(Y)
res = 0
t1 = time.time()
for i in range(cnt):
    res+=X[i-1]*Y[i-1]
t2 = time.time()

print("time: "+str(t2-t1)+"ns.")
print(res)