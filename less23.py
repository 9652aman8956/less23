lst = [12,14,15,16,66,777,87,34,234,123]                                                         
# print(max(lst))
small = lst[0]
for num in lst:
    if num < small:
        small = num
print(small)

# lst = [12,14,15,16,66,777,87,34,234,123]
# print(min(lst))
