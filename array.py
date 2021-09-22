a= eval(input("Enter list a = "))
a.sort()
print(a)
P= int(input("Enter number P = "))
def arrays(a,P):
    index = len(a)
    for x in a:
        if x>= P:
            index= a.index(x)
            break
    return index
arr= arrays(a,P)
print("Index value is",arr)