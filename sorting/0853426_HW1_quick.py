# use last element as pivot
def partition(_list, low, high):
    i = low-1
    _list[high], _list[(low+high)//2] = _list[(low+high)//2], _list[high]
    pt = _list[high]
    for j in range(low, high):
        if _list[j] <= pt:
            i += 1
            _list[i], _list[j] = _list[j], _list[i]     # SWAP
    _list[i+1], _list[high] = _list[high], _list[i+1]
    return i+1      # 切下去


def quickSort(_list, low, high):
    if low < high:
        pi = partition(_list, low, high)
        quickSort(_list, low, pi-1)
        quickSort(_list, pi+1, high)
