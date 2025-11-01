def deepEquals(obj1, obj2):
    if type(obj1) != type(obj2):
        return False

    if isinstance(obj1, dict):
        if obj1.keys() != obj2.keys():
            return False
        for key in obj1:
            if not deepEquals(obj1[key], obj2[key]):
                return False
        return True

    if isinstance(obj1, list):
        if len(obj1) != len(obj2):
            return False
        for item1, item2 in zip(obj1, obj2):
            if not deepEquals(item1, item2):
                return False
        return True

    return obj1 == obj2

