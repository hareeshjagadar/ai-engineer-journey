def contains_duplicate(nums):
    seen = set()
    for num in nums:
        # Step 1: if num is already in seen → what should you return?
        if num in seen:
            return True 

        # Step 2: otherwise → what should you do with num?
        seen.add(num)
    return False

print(contains_duplicate([1, 2, 3, 1]))  # True
print(contains_duplicate([1, 2, 3, 4]))  # False
print(contains_duplicate([]))            # False