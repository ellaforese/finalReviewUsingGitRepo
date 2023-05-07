a=[1,2,3,4,5]
'''
Find the minimum in the list
There is a min function in the math module, but don't use that here
Practice writing code in Python
'''
def find_minimum(lst):
    min_val = lst[0]
    for i in range(len(lst)):
        if lst[i] < min_val:
            min_val = lst[i]
    return min_val

print(find_minimum(a))