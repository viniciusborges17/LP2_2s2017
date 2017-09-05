def maior_ponta(nums):
    n=0
    lista=[]
    if nums[0] > nums[len(nums)-1]:
        i=0
        while i < len(nums):
            lista.append(nums[0])
            i = i + 1
    else:
        i=0
        while i < len(nums):
            lista.append(nums[len(nums)-1])
            i = i + 1
    
    return lista