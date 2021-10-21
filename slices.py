nums = [1,2,3,4,5,6]
print(nums[1:3])
print(nums[:3])
print(nums[:-3])
print(nums[3:])
print(nums[::1])
print(nums[::3])
print(nums[::4])

def slice(array, start, stop, step=1):
    if start < 0:
        start = len(array) + start

    if stop < 0:
        stop = len(array) + stop

    result = []
    index = start
    if step >= 0:
        while index < stop:
            result.append(array[index])
            index += step
    else:
        while index > stop:
            result.append(array[index])
            index += step

    return result
