def findKthLargest(nums: list[int], k: int) -> int:
    nums.sort(reverse=True)
    return nums[k - 1]


# Function to find the minimum and maximum elements
def findMinMax(nums: list[int]) -> tuple[int, int]:
    return min(nums), max(nums)


# Example list
nums = [15, 3, 8, 12, 5, 20]
k = 4

# Display the kth largest element
print("Kth Largest:", findKthLargest(nums, k))

# Display the minimum and maximum elements
print("Min-Max:", findMinMax(nums))