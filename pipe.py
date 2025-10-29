def compose(*functions):
    def composed_function(arg):
        result = arg
        for func in reversed(functions):
            result = func(result)
        return result
    return composed_function

def pipe(*functions):
    def piped_function(arg):
        result = arg
        for func in functions:
            result = func(result)
        return result
    return piped_function

if __name__ == "__main__":
    def add_one(x):
        return x + 1

    def square(x):
        return x * x

    add_then_square = pipe(add_one, square)
    square_then_add = compose(square, add_one)

    print(add_then_square(3))  
    print(square_then_add(3))  