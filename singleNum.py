def singleNumber(nums):

    # What is ^ doing? XOR?

    res = 0
    print(nums)
    for i in nums:
        print("---")
        print(res,"^=",i)
        res ^= i
        print(res)
        
    return res

nums = [4,2,2,1,3,3,1,8,8]

answer = str(singleNumber(nums))
print("! "+answer+" !")