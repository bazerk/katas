def qsort(list):
    if len(list) <= 1:
        return list
    pivot = list[0]
    return qsort(filter(lambda (x): x < pivot, list)) + filter(lambda (x): x == pivot, list) + qsort(filter(lambda (x): x > pivot, list))

def swap_elems(list, ix1, ix2):
    temp = list[ix1]
    list[ix1] = list[ix2]
    list[ix2] = temp


def qsort2(list, start=None, end=None):
    start = 0 if start is None else start
    end = len(list)-1 if end is None else end

    if start < end:
        pivot = list[start] 
        swap_elems(list, start, end)
        store_index = start
        for ix in range(start, end):
            if list[ix] < pivot:
                swap_elems(list, ix, store_index)
                store_index = store_index + 1
        swap_elems(list, end, store_index)
        qsort2(list, start, store_index)
        qsort2(list, store_index+1, end)
