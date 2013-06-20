def isset(array, *index):
    "checking if array contains element by given index (can be multidimensional)"
    try:
        element = array[index[0]]
    except Exception:
        return False
    else:
        if len(index) > 1:
            return isset(element, *index[1:])
        else:
            return True