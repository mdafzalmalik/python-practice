lst = [98, 67, 89, 85, "abcd", True, 78.0]

print(len(lst))
print(type(lst))
print(lst[5:])
print(lst[3:7])


nums = [1, 2, 3, 4]

nums.append(5)
print(nums)

nums.insert(3, 10)
print(nums)

nums.reverse()
print(nums)

nums.sort()
print(nums)

nums.sort(reverse=True)
print(nums)