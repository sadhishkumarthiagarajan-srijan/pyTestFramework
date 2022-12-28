def removedup(str):
    s=set()
    lists=[]
    for ch in str:
        if ch not in s:
            s.add(ch)
            lists.append(ch)
    return ''.join(lists)
            


def rmdp(str):
    return ''.join(set(str))

     
str="jaaay"
print(rmdp(str))



