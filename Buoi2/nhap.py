# cau 1 
# s1 = 'abc'
# s2 = 'efg'

# s = s2[:2]+s1[-1] +" " +s1[:2]+s2[-1]
# print(s)

# cau 2
# str1 = 'python'
# s =''
# for i in range(len(str1)):
#     if(i%2!=0):
#         s+=str1[i]
# print(s)

# cau 3
# s = 'no pain no gain'
# s = s.split(" ")

# t = {}

# for x in s:
#     i = s.count(x)
#     t[x] = i

# print(t)

# cau 4 
# s = 'def'
# s1  = ''
# for x in s:
#     s1+= chr(ord(x)-3)
# print(s1)

# cau 5
# S = {'0','1','2'}
# s1 = input("Hay nhap chuoi vao: ")
# k =1
# for x in s1:
#     if x not in S:
#         k=0
#         print("chuoi khong hop le!")
#         break
# if k == 1:
#     print("chuoi hop le")

# cau 6
# s = 'This is a list'
# s = s.split(" ")
# print(s)

# cau 7 
# s = input("Hay nhap chuoi vao : ")
# s1 ={}
# for x in s:
#     s1[x]= s.count(x)

# for i in s1:
#     if s1[i]==1:
#         print(i)
#         break

# cau 8
# s = 'a b c'
# s = s.replace(" ","")
# print(s)

# cau 9 
# s = 'ab ca bc ab'
# s = s.split(" ")
# s1 = set()

# for x in s:
#     if x in s1:
#         print(x)
#         break
#     s1.add(x)

# cau 10 
# s = '1110001110000'

# current  = 0
# max1 = 0
# for x in s:
#     if x =='0':
#         current+=1
#         max1 = max(max1, current)
#     else:
#         current = 0

# print(max1)

import itertools

# A = ['110','0011','0110']

# A_temp = list(itertools.permutations(A, len(A)))
# s1 = set()
# for x in A_temp:
#     str1 = "".join(list(x))
#     s1.add(str1)

# B = ['110110','00','110']
# B_temp = list(itertools.permutations(B, len(B)))
# s2 =set()
# for x in B_temp:
#     str2 = "".join(list(x))
#     s2.add(str2)
# s3 = s1.intersection(s2)

# if(len(s3)!=0):
#     print("co")
# else:
#     print("khong")

# cau 2: 

S = ['A','C','G','T']
L1 = list(itertools.combinations(S, 3))

L2 = []
for x in L1:
    L3 = list(itertools.permutations(x,len(x)))
    L2.append(L3)

L3 = []
for i in L2:
    for j in i:
        str1 = "".join(list(j))
        L3.append(str1)
print(L3)
s = input("nhap chuoi vao : ")
chuoidau=s[:3]
chuoicuoi = s[-3:]
print(chuoidau, chuoicuoi)
k=1
if(len(s)>=9):
    if(chuoidau=='ATG' and (chuoicuoi=='TAA'or chuoicuoi=='TAG' or chuoicuoi=='TGA')):
        for i in range(0,len(s),3):
            str5 = s[i]+s[i+1]+s[i+2]
            print(str5)
            if(str5 not in L3):
                k = 0
                break
else:
    k = 0

if k ==1 :
    print("hop le")
else:
    print("khong")