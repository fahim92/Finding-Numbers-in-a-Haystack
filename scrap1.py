import re
sum=0
fhand=open('regex_sum_505369.txt')
for line in fhand:
    lst=re.findall('[0-9]+',line)
    for num in lst:
        sum=sum+int(num)
print(sum)
