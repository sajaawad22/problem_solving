def Collatz (n):
    max_length =0
    starting_number =0
    for i in range(1,n):
        length =1
        num = i
        while num != 1:
            if num % 2 == 0:
                num = num // 2
            else:
                num = 3 * num + 1
            length += 1
        if length > max_length:
            max_length = length
            starting_number = i

    return starting_number,

print(Collatz(1000000))

# Output: 837799