#二叉树的最近公共祖先
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root: return root
        if root.val == p.val or root.val == q.val: return root
        l = self.lowestCommonAncestor(root.left, p, q)
        r = self.lowestCommonAncestor(root.right, p, q)
        if l and r: return root
        if l: return l
        if r: return r


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        if len(nums) < 4: return []
        nums.sort()
        result = []

        for idx in range(len(nums) - 3):
            if nums[idx] + nums[idx+1] * 3 > target: break  # 这是加速项目，如果当前位置的数字+剩余位置数位的下一个数的倍数>target，则分析当前位置无意义
            if idx > 0 and nums[idx] == nums[idx - 1]: continue  # 如果当前的索引已经不是第一位的了，就要走到一个跟上一个不一样数字的索引上去
            if nums[idx] + nums[-1] * 3 < target: continue  # 这是加速项目，如果当前位置的数字+剩余位置数位的最后（大）数的倍数<target，则分析当前位置无意义

            for i in range(idx+1, len(nums)-2):
                if nums[idx] + nums[i] + nums[i + 1] * 2 > target: break
                if nums[idx] + nums[i] + nums[-1] * 2 < target: continue
                if i > idx+1 and nums[i] == nums[i-1]: continue

                j, k = i + 1, len(nums) - 1
                while j < k:
                    s = nums[idx] + nums[i] + nums[j] + nums[k]
                    if s > target:
                        k -= 1
                    elif s < target:
                        j += 1
                    else:
                        result.append([nums[idx], nums[i], nums[j], nums[k]])
                        while j < k and nums[j] == nums[j + 1]: j += 1
                        while j < k and nums[k] == nums[k - 1]: k -= 1
                        j += 1
                        k -= 1
        return result

    class Solution:
        def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
            if len(nums) < 4: return []
            nums.sort()
            result = []

            for idx in range(len(nums) - 3):
                if nums[idx] + nums[idx + 1] * 3 > target: break  # 这是加速项目，如果当前位置的数字+剩余位置数位的下一个数的倍数>target，则分析当前位置无意义
                if idx > 0 and nums[idx] == nums[idx - 1]: continue  # 如果当前的索引已经不是第一位的了，就要走到一个跟上一个不一样数字的索引上去
                if nums[idx] + nums[-1] * 3 < target: continue  # 这是加速项目，如果当前位置的数字+剩余位置数位的最后（大）数的倍数<target，则分析当前位置无意义

                for i in range(idx + 1, len(nums) - 2):
                    if nums[idx] + nums[i] + nums[i + 1] * 2 > target: break
                    if nums[idx] + nums[i] + nums[-1] * 2 < target: continue
                    if i > idx + 1 and nums[i] == nums[i - 1]: continue

                    j, k = i + 1, len(nums) - 1
                    while j < k:
                        s = nums[idx] + nums[i] + nums[j] + nums[k]
                        if s > target:
                            k -= 1
                        elif s < target:
                            j += 1
                        else:
                            result.append([nums[idx], nums[i], nums[j], nums[k]])
                            while j < k and nums[j] == nums[j + 1]: j += 1
                            while j < k and nums[k] == nums[k - 1]: k -= 1
                            j += 1
                            k -= 1
            return result





from typing import List


class Solution(object):
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:

        length = len(nums)
        # result = set()
        result = []

        # 双指针法使用前提：排序
        nums.sort()

        for i in range(length - 3):
            # 去重（剪枝）
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            # 如果固定数与数组三最小数之和大于target, 则后续循环都是不存在解的, 从遍历中跳出
            if nums[i] + sum(nums[i + 1:i + 3 + 1]) > target:
                break
            # 如果固定数与数组三最大数之和小于taget, 则当前遍历不存在解, 进入下一个遍历
            if nums[i] + sum(nums[-1:-3 - 1:-1]) < target:
                continue

            for j in range(i + 1, length - 2):
                # 去重（剪枝）
                if j - i > 1 and nums[j] == nums[j - 1]:
                    continue
                # 如果固定数与数组两最小数之和大于target, 则后续循环都是不存在解的, 从遍历中跳出
                if nums[i] + nums[j] + sum(nums[j + 1:j + 2 + 1]) > target:
                    break
                # 如果固定数与数组两最大数之和小于target, 则当前遍历不存在解, 进入下一个遍历
                if nums[i] + nums[j] + sum(nums[-1:-2 - 1:-1]) < target:
                    continue

                # 双指针法
                left, right = j + 1, length - 1
                while left < right:
                    tmp_sum = nums[i] + nums[j] + nums[left] + nums[right]
                    # 如果当前和小于target, 收缩左边界
                    if tmp_sum < target:
                        left += 1
                    # 如果当前和大于target, 收缩左边界
                    elif tmp_sum > target:
                        right -= 1
                    # 如果值相等
                    else:
                        # 记录解
                        # result.add((nums[i], nums[j], nums[left], nums[right], ))
                        result.append([nums[i], nums[j], nums[left], nums[right]])

                        # 求得正确解后，去重（剪枝）
                        while left < right and nums[left] == nums[left + 1]:
                            left += 1
                        # 求得正确解后，去重（剪枝）
                        while left < right and nums[right] == nums[right - 1]:
                            right -= 1

                        # 在求得正确解，并且剪枝后，仅收缩移动一个指针，都不会是正确解；
                        # 因此应收缩移动双指针，直接排除不符合解的情况，减少运算次数
                        left += 1
                        right -= 1

        return result

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        n=len(nums)
        if(not nums or n<4):
            return []
        nums.sort()
        res=[]
        for i in range(n-3):
            if(nums[i]+nums[i+1]+nums[i+2]+nums[i+3]>target):
                break
            if(nums[i]+nums[-1]+nums[-2]+nums[-3]<target):
                continue
            if(i>0 and nums[i]==nums[i-1]):
                continue
            for j in range(i+1,n-2):
                if(nums[i]+nums[j]+nums[j+1]+nums[j+2]>target):
                    break
                if(nums[i]+nums[j]+nums[-1]+nums[-2]<target):
                    continue
                if(j-i>1 and nums[j]==nums[j-1]):
                    continue
                L=j+1
                R=n-1
                while(L<R):
                    if(nums[i]+nums[j]+nums[L]+nums[R]==target):
                        res.append([nums[i],nums[j],nums[L],nums[R]])
                        while(L<R and nums[L]==nums[L+1]):
                            L=L+1
                        while(L<R and nums[R]==nums[R-1]):
                            R=R-1
                        L=L+1
                        R=R-1
                    elif(nums[i]+nums[j]+nums[L]+nums[R]>target):
                        R=R-1
                    else:
                        L=L+1
        return res


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        n = len(nums)
        if (not nums or n < 4):
            return []
        nums.sort()
        result=[]
        for i in range(n - 3):
            if (nums[i] + nums[i + 1] + nums[i + 2] + nums[i + 3] > target):
                break
            if (i > 0 and nums[i] == nums[i - 1]):
                continue
            if (nums[i] + nums[i + 1] + nums[i + 2] + nums[i + 3] < target):
                continue
            for c in range(i + 1, n - 2):
                if (nums[i] + nums[c] + nums[c + 1] + nums[c + 2] > target):
                    break
                if (c - i > 1 and nums[c] == nums[c - 1]):
                    continue
                if (nums[i] + nums[c] + nums[c + 1] + nums[c + 2] < target):
                    continue
                j = c + 1
                k = n - 1
                n - 1
                while j < k:
                    s = nums[i] + nums[c] + nums[j] + nums[k]
                    if s == target:
                        result.append([nums[i], nums[c], nums[j], nums[k]])
                        while j < k and nums[j] == nums[j + 1]:
                            j += 1
                        while j < k and nums[k] == nums[k - 1]:
                            k -= 1
                        j += 1
                        k -= 1
                    elif s > target:
                        k -= 1
                    else:
                        j += 1

        return result