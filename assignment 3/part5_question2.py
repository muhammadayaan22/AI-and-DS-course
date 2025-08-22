nums = [32, 54, 66, 11, 77, 10, 90]
nw_nums = []
for n in nums:
    if n >= 20:
        nw_nums.append(n)

print("Values less then 20:", nw_nums)
print("Ascending:" , sorted(nw_nums))
print("Descending:" , sorted(nw_nums, reverse=True))

print("Average:" , sum(nw_nums))
