r, c, n = map(int,input().split())
taken = set()
day = 1
for i in range(n):
    a, b = map(int, input().split())
    square = (a,b)
    taken.add(square)
while(len(taken)<(r*c)):
    today = set()
    for i in taken:
        if(i[0]<r):
            today.add((i[0]+1, i[1]))
        if(i[0]>1):
            today.add((i[0]-1, i[1]))
        if(i[1]<c):
            today.add((i[0], i[1]+1))
        if(i[1]>1):
            today.add((i[0], i[1]-1))
    taken.update(today)
    day+=1
print(day)