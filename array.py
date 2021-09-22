a= eval(input("Enter list a = "))
a.sort()
print(a)
P= int(input("Enter number P = "))
def arrays(a,P):
    for x in a:
        if x>= P:
            index= a.index(x)
            print("Index value is",index)
            return index
        else:
            index= len(a)
    print("Index value is",index)
arrays(a,P)