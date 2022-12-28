
s="ind";
def pali(s):
    return s==s[::-1]
ans =pali(s)
print(ans)
if ans:
    print("yes")
else:
    print("no")