def dirReduc(arr):
    opposite = {"NORTH": "SOUTH", "SOUTH": "NORTH", "EAST": "WEST", "WEST": "EAST"}
    stack = []
    
    for direction in arr:
        if stack and stack[-1] == opposite[direction]:
            stack.pop()
        else:
            stack.append(direction)
    
    return stack