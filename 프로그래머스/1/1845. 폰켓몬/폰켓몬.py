def solution(nums):
    len_n=len(nums) 
    nums=set(nums)
    return min(len(nums),len_n//2)