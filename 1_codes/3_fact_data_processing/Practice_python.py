l = [7, 6, 4, 1, 3, 8, 11, 7, 7, 9, 6, 4, 7, 13, 16, 8]
r = [4, 3, 8, 11, 7, 7, 9, 6, 4, 7, 13, 16, 8]

result = list(zip(l,r))
result.sort(key=lambda x:x[1])
last = -float('inf')
print(result)
count = 0
for start,end in result:
    if start>=last:
        last = end
        count+=1

print("count",count)