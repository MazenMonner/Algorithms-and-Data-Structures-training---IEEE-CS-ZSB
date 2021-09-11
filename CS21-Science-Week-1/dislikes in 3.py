test_case = int(input())
number=[]

for j in range(0,test_case):
    num = int(input())
    number.append(num)
    
largest_number = max(number)
first_sequence = []
x=1 
for i in range(0,largest_number+1):
    if x%10 != 3 and x%3!=0:
        first_sequence.append(x)
        x+=10
    else :
        x==1
        if x %10 != 3 and x%3!=0:
            first_sequence.append(x)
            x+=1
        else : 
            x+=1 
            if x%10!=3 and x%3!=0:
                first_sequence.append(x)
                x++1
                
for j in range(0,test_case):
    numbers = int(number[j]-1)
    print (first_sequence[numbers])
