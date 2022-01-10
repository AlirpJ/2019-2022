# DOES NOT WORK


def can_reach_end(nums):
    canJump = True
    currentPlace = 0
    canReach = False
    
    while canJump:
        print(currentPlace)
        print(nums[currentPlace])
        print("---")
        if currentPlace >= len(nums):
            canJump = False
            canReach = True
        if nums[currentPlace] > 0:
            currentPlace = currentPlace + nums[currentPlace]
        else:
            canJump = False
            
    return canReach


can_reach_end([1,2,3])

