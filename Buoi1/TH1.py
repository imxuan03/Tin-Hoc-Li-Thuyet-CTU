# string = 'I am a student'
# print(string)

#cau 1
# s1 = 'abc'
# s2 = 'efg'
# s3 = s2[:2] + s1[-1] + ' ' + s1[:2] + s2[-1]

# print(s3)


#cau 2
# string = 'python'
# s1 = ''
# for i in range(len(string)):
#     if i % 2 != 0 :
#         s1+=string[i]

# print(s1)

# cau 3 
# s = 'no pain no gain'
# s = s.split(" ")
# s1 = {}
# for i in s:
#     s1[i] = s.count(i)

# print(s1)

# cau 4 (ve lam lai)
# s ='def'
# s1 = ''
# for i in s:
#     s1+=chr(ord(i)-3)

# print(s1)

# cau 5
# s = {'0','1','2'}
# chuoi = input("Nhap chuoi vao: ")
# x = 1
# for i in range(len(chuoi)):
#     k = 0
#     for j in s:
#         if chuoi[i]==j:
#             k = 1
    
#     if k == 0:
#         x = 0
#         break

# if x  == 0:
#     print("Khong hop le")
# else :
#     print("Hop le")


# cau 6
# s = 'This is a list'
# s = s.split(" ")
# print(s)

# cau 7
# s = input("Nhap chuoi : ")
# s1 = {}

# for i in s :
#     s1[i] = s.count(i)

# for i in s1:
#     if s1[i] ==1:
#         print(i)
#         break

# cau 8 
# s = 'a b c'
# print(s.replace(" ",""))

# cau 9
# s = input("Nhap vao chuoi : ")
# s = s.split(" ")
# tudaxem = set()

# for s in s:
#     if s in tudaxem :
#         print(s)
#         break
    
#     tudaxem.add(s)

# cau 10 
# s = input('Nhap chuoi : ')

# count =[]
# k = 0
# for i in range(len(s)-1):
#     if (s[i] == '0' and s[i+1]=='0'):
#         k+=1
#     elif s[i] == '0' and  s[i+1] =='1':
#         count.append(k)
#         k=0
#         continue

#     count.append(k) #truong hop 000 nam o cuoi cung vd 11001100000=>5

# max = -1
# for i in count:
#     if max< i:
#         max = i

# print(max+1) #cong mot cai ban dau nua