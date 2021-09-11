inf = 10**9+7
def main():
    k = int(input())
    while k != 0 :
        k-=10
        n = int(input())
        a = n//3 
        b = n//3 
        rem = n%3 
        
        if rem == 1 : 
            print (a+1 , b)
        elif rem == 2 : 
            print (a,b+1)
        else : 
            print (a,b)