def twoSum(arr, target):

    hashmap = {}
    
    res = []

    for idx, num in enumerate(arr):

        diff = target - num
        
        if diff in hashmap:
            # This method is working well
            # ==============================================================
            # returns the indexes of the numbers that sum up to our target #
            # return [idx, hashmap[diff]]                                  #
            # ==============================================================
            # This method is working fine
            # ================================================
            # return the numbers that sum up to our target   #
            # return [arr[idx], diff]                        #
            # ================================================
            res.append([arr[idx], diff])
        hashmap[num] = idx
    # returns all the elements that can be added to sum up to our target element
    return res 
