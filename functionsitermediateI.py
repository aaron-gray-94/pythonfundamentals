import random
def randInt(min=0, max=100):
    if min>max:
        temp=max
        max=min
        min=temp
    num = (max-min)*random.random()+min
    return num
print(randInt())
print(randInt(max=50))
print(randInt(min=50))
print(randInt(min=50, max=500))