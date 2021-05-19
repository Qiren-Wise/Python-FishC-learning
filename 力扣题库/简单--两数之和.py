def twoSum(nums,target):
    lens=len(nums)
    x = -1
    for i in range(lens):
        temp = nums[:i]
        if (target - nums[i]) in temp:
            x = temp.index(target - nums[i])
            break

    if x>=0:
        return [x,i]

print(twoSum(nums=[5,2,15,7],target=9))

'''
本解法是先利用lens的值来进行循环，每循环一次i就会+1，直到找到其中一个索引值，另一个索引值靠index这个字符串内置方法来
找到另一个索引值
'''
