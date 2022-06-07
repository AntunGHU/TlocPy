def max_magnitude(nums):
    return max(abs(num) for num in nums)

    
max_magnitude([300, 20, -900])   #900
max_magnitude([10, 11, 12])   #12
max_magnitude([-5, -1, -89])   #89
