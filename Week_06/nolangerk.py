#矩形区域不超过K的最大值和
class Solution:
    def maxSumSubmatrix(self, matrix: List[List[int]], k: int) -> int:

        def maxSubArraylessK(nums, k):
            cumset = [0]
            maxsum = -1 << 32
            cursum = 0
            for i in range(len(nums)):
                cursum += nums[i]
                idx = bisect.bisect_left(cumset, cursum - k)
                if 0 <= idx < len(cumset):
                    maxsum = max(maxsum, cursum - cumset[idx])
                if maxsum == k:
                    break
                bisect.insort(cumset, cursum)
            return maxsum

        row, col = len(matrix), len(matrix[0])
        res = -(1 << 32)
        for left in range(col):
            cursums = [0 for _ in range(row)]
            right = left
            while right < col:
                for i in range(row):
                    cursums[i] += matrix[i][right]
                curarrmax = maxSubArraylessK(cursums, k)
                res = max(res, curarrmax)
                right += 1

        return res