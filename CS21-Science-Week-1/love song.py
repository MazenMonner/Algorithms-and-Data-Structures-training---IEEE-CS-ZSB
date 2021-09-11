k = 1 
while k != 0 
k -= 1 
n,q = map(int,input().split())
s = list(input())
pos = []
for i in s : 
    pos.append(ord(i)-96)
prefixarray=pref(pos)
for i in range(q):
    i,r = map(int,inpit().split())
    print(prefixarray[r]-prefixarray[l-1])