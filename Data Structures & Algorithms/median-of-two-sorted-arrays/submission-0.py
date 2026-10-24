class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = nums1, nums2

        if len(B) < len(A):
            A, B = B, A

        total = len(A) + len(B)
        half = total // 2

        left, right = 0, len(A) - 1

        while True:
            a_idx = left + (right - left) // 2
            b_idx = half - a_idx - 2

            a_left = A[a_idx] if a_idx >= 0 else float("-inf")
            a_right = A[a_idx + 1] if a_idx + 1 < len(A) else float("inf")

            b_left = B[b_idx] if b_idx >= 0 else float("-inf")
            b_right = B[b_idx + 1] if b_idx + 1 < len(B) else float("inf")


            if a_left <= b_right and b_left <= a_right:
                if total % 2:
                    return min(a_right, b_right)
                return (max(a_left, b_left) + min(a_right, b_right)) / 2
            elif a_left > b_right:
                right = a_idx - 1
            else:
                left = a_idx + 1

        

