import itertools

#Bai1 nang cao
# L1 = ['110','0011','0110']
# L1_temp = list(itertools.permutations(L1,len(L1)))
# S1 = set()

# for i in L1_temp:
#     str1 = "".join(list(i))
#     S1.add(str1)
# print(S1)

# L2 = ['110110','00','110']
# L2_temp= list(itertools.permutations(L2,len(L2)))
# S2 = set()

# for i in L2_temp:
#     str2 = "".join(list(i))
#     S2.add(str2)
    
# S3 = S1.intersection(S2)
# if(len(S3)!=0):
#     print("YES")
# else:
#     print("NO")


# Bai2 nang cao 
S = ['A','C','G','T']
S_temp = list(itertools.combinations(S,3))

L = []
for i in S_temp:
    str1 = list(itertools.permutations(list(i),len(list(i))))
    L.append(str1)
    
# print(L)

L1 = []
for i in L:
    for j in i:
        str2 = "".join(list(j))
        L1.append(str2)
        
print(L1)

k=0
chuoi = input("Nhap vao :")
chuoicuoi = chuoi[-3:-1]+chuoi[-1]
if(chuoi[:3]=='ATG' and (chuoicuoi=='TAA' or chuoicuoi=='TAG' or chuoicuoi=='TGA' )):
    for i in range(0,len(chuoi),3):
        str3 = chuoi[i]+chuoi[i+1]+chuoi[i+2]
        print(str3)
        if(str3 not in L1):
            k=0
        elif str3 in L1:
            k = k+1
else:
    k=0

print(k)
if(k >2):
    print("Hop le")
else:
    print("Khong Hop Le")