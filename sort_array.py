class Solution:
    # Function to sort an array of 0s, 1s, and 2s
    def sort012(self, arr):
        # Initialize pointers
        low = 0       # Position for the next 0
        mid = 0       # Current element
        high = len(arr) - 1  # Position for the next 2

        # Iterate until mid pointer crosses high pointer
        while mid <= high:
            if arr[mid] == 0:
                # Swap to place 0 in the low section
                arr[low], arr[mid] = arr[mid], arr[low]
                low += 1
                mid += 1
            elif arr[mid] == 1:
                # Move to the next element if 1
                mid += 1
            else:  # arr[mid] == 2
                # Swap to place 2 in the high section
                arr[mid], arr[high] = arr[high], arr[mid]
                high -= 1

# Test:
arr = [0, 1, 2, 0, 1, 2, 0, 2, 1]
sol = Solution()
sol.sort012(arr)
print(arr)  # Output should be: [0, 0, 0, 1, 1, 1, 2, 2, 2]
