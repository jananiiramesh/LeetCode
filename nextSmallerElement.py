def next_smallest(nums):
    nse = {num: -1 for num in nums}
    stack = []
    for num in nums:
        while stack and num < stack[-1]:
            prev = stack.pop()
            nse[prev] = num
        stack.append(num)

    return [nse[num] for num in nums]
