n = list(map(int, input().split()))
x1 = n[0]
y1 = n[1]
r1 = n[2]

for i in range(0,3):
    n[i]*=n[i+3]
    n[i+3]*=n[i]

y2=n[1]-n[4]
r2=n[2]-n[5]

y2=r2//y2
x2=(r1-(y1*y2))//x1

print(x2,y2)
