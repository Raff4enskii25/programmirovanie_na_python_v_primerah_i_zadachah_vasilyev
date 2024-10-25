nums = set(i for i in range(50+1))
nums1 = set()
print(nums)
for i in nums:
    if (i%3==0 or i%11==0) and i%5!=0 and i%7 !=0:
        nums1.add(i)
print("Числа, которые делятся на 3 и 11, но не делятся на 5 и 7:", nums1)