sentence=input("State the sentence: ")
list1=sentence.split()
var1=len(list1)
if(var1%2==0):
    m=var1/2
    n=int(m-1)
    print(list1[n]+" "+list1[n+1])
else:
    m=int(var1/2)
    print(list1[m])
sortedwords=sorted(list1, key=len)
print(sortedwords[-1])
list2=''
list3=''
var2=len(list1)
n=0
for m in range(var2):
    list2=list1[n][::-1]
    print(list2)
    n=n+1
