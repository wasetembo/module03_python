class Solution:
    def binarysearch(self, arr, k):
        left, right = 0, len(arr) - 1
        result = -1  # Initialize result as -1 to handle cases where k is not found

        while left <= right:
            mid = left + (right - left) // 2  # Calculate mid-point

            if arr[mid] == k:
                result = mid  # Found an occurrence of k
                right = mid - 1  # Move to the left side to find the smallest index
            elif arr[mid] < k:
                left = mid + 1  # Search in the right half
            else:
                right = mid - 1  # Search in the left half

        return result  # Return the smallest index of k if found, or -1 if not found

# test
arr = [1, 2, 2, 2, 3, 4, 5]
k = 2
sol = Solution()
print(sol.binarysearch(arr, k))  # Output should be 1, the smallest index of k
