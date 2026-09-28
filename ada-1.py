
# Binary Search

def search(nums, target, low, high):
    if low > high:
        return -1

    mid = (low + high) // 2

    if nums[mid] == target:
        return mid
    elif target < nums[mid]:
        return search(nums, target, low, mid - 1)
    else:
        return search(nums, target, mid + 1, high)


# Power Function

def myPow(x, n):
    if n == 0:
        return 1

    half = myPow(x, n // 2)

    if n % 2 == 0:
        return half * half
    else:
        return x * half * half


nums = list(map(int, input("Enter sorted array: ").split()))
target = int(input("Enter target: "))

result = search(nums, target, 0, len(nums) - 1)

if result != -1:
    print("Element found at index", result)
else:
    print("Element not found")

x = int(input("\nEnter base: "))
n = int(input("Enter exponent: "))

if n >= 0:
    print("Power =", myPow(x, n))
else:
    print("Power =", 1 / myPow(x, -n))