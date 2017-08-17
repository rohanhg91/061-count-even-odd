def solution(list_of_nums):
    """Enter Code Here"""
    even = []
    odd = []

    for i in list_of_nums:
        if i % 2 == 0:
            even.append(i)
        else:
            odd.append(i)

    num_even = len(even)
    num_odd = len(odd)
    return {'ODD': num_odd, 'EVEN': num_even}

'''
a = solution([1,2,3,4,5,6,7])
print a
'''
