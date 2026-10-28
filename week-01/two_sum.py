def two_sum(nums, target):
    seen = {}  # number -> index
    for i, num in enumerate(nums):

        
        # Step 1: what number do you NEED to pair with num?
        needed = target - num
        # Step 2: if that number is in seen → return [?, ?]
        if needed in seen:
            return [seen[needed], i]
        # Step 3: otherwise → store num with its index
        seen[num] = i
print(two_sum([2, 7, 11, 15], 9))  # [0, 1]
print(two_sum([3, 2, 4], 6))       # [1, 2]
print(two_sum([3, 3], 6))          # [0, 1]