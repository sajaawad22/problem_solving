def flatten(*args):
    result = []
    
    def _flatten(item):
        if isinstance(item, list):
            for sub_item in item:
                _flatten(sub_item)
        else:
            result.append(item)
    
    for arg in args:
        _flatten(arg)
    
    return result