# a list of 10 will print out 1-9

nums1 = [x for x in range(10)]
print(nums1)

sum1 = 0
for num in nums1:
    sum1 += num  # sum1 = sum1 + num

print(sum1)

nums2 = [3, 4, 5, 6, 23, 45, 234, 4534, 45]
sum2 = 0

for num in nums2:
    sum2 = sum2 + num

avg = sum2 / len(nums2)

avg = 1 * 2 * 3 * 4
# 3 + 3 + 4
# 6 + 4
# 10


def summation(nums):
    x = 0
    for n in nums:
        x += n

    return x


nums3 = [2, 4, 5, 2, 343, 54]

avg = summation(nums3) / len(nums3)

total = summation(nums1) + summation(nums2) + summation(nums3)
