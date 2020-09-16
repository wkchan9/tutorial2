def two_sum(nums: list, tar):
    numss = []
    for i, k in enumerate(nums):
        if k < tar: numss.append((i, k))
        if k == tar: return [i]
    numss.sort(key = (lambda i: i[1]))
    cou = 2**len(numss)
    while cou > 0:
        result = []
        tem = 0
        for k, i in enumerate("{0:b}".format(cou)):
            if i == '1':
                result.append(numss[k][0])
                tem += numss[k][1]
        if tem == tar: return result
        else: cou -= 1
    return result

#at least 1 solution, elements in nums and target >= 0
nums = list(map(int, input().split()))
tar = int(input())
print(two_sum(nums, tar))
