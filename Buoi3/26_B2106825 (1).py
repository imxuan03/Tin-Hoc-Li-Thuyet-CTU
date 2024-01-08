import itertools

def countsub(s1,sub):
    count = 0
    lenght = len(sub)
    for i in range(len(s1)-lenght+1):
        if s1[i:i+lenght]==sub:
            count+=1    

    return count



s1 = '100010101011010110010001111010'
sub1 ='010'
print(countsub(s1,sub1))

s2 = '10001010101101011'
sub2 ='010'
print(countsub(s2,sub2))

s3 = '1230001230986123'
sub3 ='123'
print(countsub(s3,sub3))