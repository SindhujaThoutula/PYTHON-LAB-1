P1=['Saketh','Surya','Sindhu','Pavan','Ankitha','Bachina','Akash']
W1=['Anjan','Aditi','Pavan','Ankitha','Rohith','Valli']
var1=len(W1)
var2=len(P1)
a=0
same_list=[]
diff_list=[]
for i in range(var1):
    if W1[a] in P1:
        same_list.append(W1[a])
    else:
        diff_list.append(W1[a])
    a=a+1
b=0
for j in range(var2):
         if P1[b] not in W1:
          diff_list.append(P1[b])
          b=b+1
print(same_list)
print(diff_list)