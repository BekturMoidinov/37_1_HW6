
def selection_sort(digits:list):
    c=len(digits)
    l=[]
    for j in range(c):
        min = digits[0]
        for i in digits:
            if min > i:
                min = i
        digits.remove(min)
        l.append(min)
    return l

def binary_search(sort,val):
    first = 0
    last = len(sort) - 1
    resultok = False
    pos=0
    while first <= last:
        mid = (last + first) // 2
        if sort[mid] == val:
            first = mid
            last = first-1
            resultok = True
            pos = mid
        elif val > sort[mid]:
            first = mid + 1
        else:
            last = mid - 1
    if resultok:
        print(f"Value is found in index {pos}")
    else:
        print("Not found")
