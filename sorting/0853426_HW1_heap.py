def heapify(_list, i, n):
    largest = i     # 最大值的index
    left = 2 * i + 1
    right = 2 * i + 2
    # 看有沒有子點，樹根vs左子點，不用小於等於是因為index的關係
    if left < n and _list[i] < _list[left]:
        largest = left
    # 在跟右子點比
    if right < n and _list[largest] < _list[right]:
        largest = right
    if largest != i:
        _list[i], _list[largest] = _list[largest], _list[i]
        heapify(_list, largest, n)      # 繼續往下探


def heapSort(_list):
    n = len(_list)
    for i in range(n, -1, -1):
        heapify(_list, i, n)
    for i in range(n-1, 0, -1):     # 從 list[n-1] 開始到 list[0] swap
        _list[i], _list[0] = _list[0], _list[i]
        heapify(_list, 0, i)
