list1 = [10,20, 56, 51, 53 ,30,40,50]

ans = []
for x in list1:
    if x % 2 != 0:
        ans.append(x)

print(ans)   # [51, 53]


res = [x for x in list1 if x % 2 != 0]
print(res)



# ----------------------

res1 = [int(i) for i in input().split(",")]
print("Answer: ",res1)