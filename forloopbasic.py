for i in range (151):
    print(i)

for i in range (0,1001,5):
    print(i)

for i in range (101):
    if i%10==0:
    	print("Coding Dojo")
    elif i%5==0:
    	print("Coding")
    else:
    	print(i)

sum=0
for i in range(1,500001,2):
    sum = sum + i
print(sum)

for i in range(2018,0,-4):
    print(i)

lowNum=1
highNum=10
mult=3
for i in range(lowNum, highNum+1):
    if i%mult==0:
        print(i)