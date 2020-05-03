def insertionSort(_list):
    for i in range(1, len(_list)):
        pk = _list[i]
        j = i - 1
        while j >= 0 and _list[i] < _list[j]:
            _list[j] = _list[i]
            j -= 1
        _list[j+1] = pk