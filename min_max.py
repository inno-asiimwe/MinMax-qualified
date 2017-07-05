def find_max_min(alist):
    """Find the maximum and minimum elements elements in a list and returns a list with the min and max elements"""
    
    if len(alist)!= 0:
        if len(set(alist)) == 1:
            return[len(alist)]
        else:
            alist.sort()
            return[alist[0], alist[-1]]
    else:
        print("list is empty")
    