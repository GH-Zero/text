# text

#给system变成/*a*/s./*a*/y./*a*/s./*a*/t./*a*/e./*a*/m/*a*/
q="system"
m=list(q)
i=0
l=len(m)*2
while i<=12:

   if i==0:
       m.insert(i,"/*a*/")
   elif 0<i<l:
       m.insert(i,"./*a*/")
   else:
        m.insert(i,"/*a*/")
   i=i+2
h=''.join(m)
print(h)
#给这些字符串变成./*a*/
q="asdfghjklzxcvbnmqwertuiopojhbvbghjjdkkskiwwuehsbxbuxbxjdjdieiehebehyyebbrkwkwbsbasuduhedjssjejsjnssjwowiwiwi"
m=list(q)
i=0
l=len(m)*2
while i<=l:
    m.insert(i,"./*a*/")

    i=i+2
h=''.join(m)
print(h)
